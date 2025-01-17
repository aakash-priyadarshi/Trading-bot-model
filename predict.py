import os
from flask import Flask, request, jsonify
from azureml.core import Workspace, Model
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pymongo import MongoClient
import mlflow
import traceback
from dotenv import load_dotenv
from pandas.tseries.offsets import BDay

# Load environment variables
load_dotenv()

app = Flask(__name__)

# MongoDB setup
mongo_uri = os.getenv('MONGO_URI')
client = MongoClient(mongo_uri)
db = client.get_default_database()
model_data_collection = db['model_ready_data']

# Load Azure ML workspace
try:
    ws = Workspace.from_config()
    print("Workspace configuration succeeded")
except Exception as e:
    print(f"Error loading workspace configuration: {e}")
    raise

# Load the model
try:
    model_name = "Time-Series-Prophet-Model"  # Replace with your actual model name
    model = Model(ws, model_name)
    model_path = model.download(exist_ok=True)
    loaded_model = mlflow.pyfunc.load_model(model_path)
    print(f"Model '{model_name}' loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")
    print("Traceback:")
    traceback.print_exc()
    raise

def get_prediction_data(symbol, days=30):
    end_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    start_date = end_date - BDay(days)  # This will give us the last 30 business days
    
    data = list(model_data_collection.find({
        'Ticker': symbol,
        'Date': {'$gte': start_date, '$lte': end_date}
    }).sort('Date', 1))

    df = pd.DataFrame(data)
    
    if df.empty:
        raise ValueError(f"No data available for {symbol} in the specified date range")
    
    # Ensure all required columns are present
    required_columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Ticker', 
                        'RSI', 'MACD_12_26_9', 'MACDh_12_26_9', 'MACDs_12_26_9', 
                        'BBL_20_2.0', 'BBM_20_2.0', 'BBU_20_2.0', 'BBB_20_2.0', 'BBP_20_2.0', 'MA']
    
    for col in required_columns:
        if col not in df.columns:
            df[col] = np.nan
    
    print(f"Fetched {len(df)} rows of data for {symbol}")
    return df

@app.route('/api/v1/trading/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        ticker = data['symbol']
        current_price = data['current_price']
        prediction_days = data.get('prediction_days', 30)  # Default to 30 days

        # Ensure prediction_days is one of the allowed values
        allowed_days = [7, 14, 21, 28, 35, 42, 49, 56]
        prediction_days = min(allowed_days, key=lambda x: abs(x - prediction_days))

        print(f"Received request for {ticker}, current price: {current_price}, prediction days: {prediction_days}")

        prediction_data = get_prediction_data(ticker, days=60)  # Fetch more data to ensure we have enough for predictions
        
        if len(prediction_data) < 20:  # Assuming we need at least 20 data points for a reliable prediction
            raise ValueError(f"Insufficient data for prediction. Only {len(prediction_data)} data points available.")

        print(f"Prediction data shape: {prediction_data.shape}")
        print(f"Prediction data columns: {prediction_data.columns}")
        print(f"Prediction data head:\n{prediction_data.head()}")
        print(f"Prediction data tail:\n{prediction_data.tail()}")

        predictions = loaded_model.predict(prediction_data)
        
        print(f"Raw predictions: {predictions}")

        if len(predictions) == 0:
            raise ValueError("Model returned no predictions")

        forecast_dates = [datetime.now().date() + timedelta(days=i) for i in range(1, prediction_days + 1)]
        
        processed_predictions = []
        for i in range(0, prediction_days, 7):
            week_predictions = predictions[i:i+7]
            week_dates = forecast_dates[i:i+7]
            
            if len(week_predictions) == 0:
                continue  # Skip this week if there are no predictions
            
            min_price = min(week_predictions)
            max_price = max(week_predictions)
            
            for j, (date, price) in enumerate(zip(week_dates, week_predictions)):
                if j < len(week_predictions):  # Ensure we don't go out of bounds
                    if price == min_price:
                        action = 'buy'
                    elif price == max_price:
                        action = 'sell'
                    else:
                        action = 'hold'
                    
                    processed_predictions.append({
                        'date': date.strftime('%Y-%m-%d'),
                        'predicted_close': float(price),
                        'action': action
                    })

        if len(processed_predictions) == 0:
            raise ValueError("No predictions were processed")

        # Calculate overall trend
        overall_trend = 'upward' if predictions[-1] > predictions[0] else 'downward'
        
        response = {
            'symbol': ticker,
            'current_price': current_price,
            'predictions': processed_predictions,
            'overall_trend': overall_trend
        }
        
        return jsonify(response)

    except Exception as e:
        print(f"Error during prediction: {str(e)}")
        print("Traceback:")
        traceback.print_exc()
        return jsonify({
            'error': str(e),
            'details': {
                'ticker': ticker if 'ticker' in locals() else 'Not set',
                'prediction_days': prediction_days if 'prediction_days' in locals() else 'Not set',
                'prediction_data_shape': prediction_data.shape if 'prediction_data' in locals() else 'Not available',
                'predictions_length': len(predictions) if 'predictions' in locals() else 'Not available'
            }
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)