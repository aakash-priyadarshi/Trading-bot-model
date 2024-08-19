#data_handler.py
import os
from datetime import datetime, timedelta
import yfinance as yf
import pandas as pd
import pandas_ta as ta
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB setup
mongo_uri = os.getenv('MONGO_URI')
client = MongoClient(mongo_uri)
db = client.get_default_database()
model_data_collection = db['model_ready_data']

def fetch_and_prepare_data(symbol, start_date, end_date):
    # Fetch historical stock data
    data = yf.download(symbol, start=start_date, end=end_date)
    
    # Calculate RSI and MACD
    data['RSI'] = ta.rsi(data['Close'])
    macd = ta.macd(data['Close'])
    
    # Add MACD, MACD_Signal, and MACD_Hist to the DataFrame
    data = pd.concat([data, macd], axis=1)
    
    # Calculate Bollinger Bands
    bollinger = ta.bbands(data['Close'], length=20, std=2)
    
    # Add Bollinger Bands to the DataFrame
    data = pd.concat([data, bollinger], axis=1)
    
    # Calculate Moving Average
    data['MA'] = ta.sma(data['Close'], length=20)
    
    # Add a column for the ticker
    data['Ticker'] = symbol
    
    # Forward fill and backward fill missing values
    data.ffill(inplace=True)
    data.bfill(inplace=True)
    
    # Reset index to have Date as a column
    data.reset_index(inplace=True)
    
    return data

def update_database():
    tickers = ['AAPL', 'AMZN', 'BRK-B', 'GOOGL', 'JNJ', 'JPM', 'META', 'MSFT', 'NVDA', 'TSLA']
    start_date = '2019-01-01'
    end_date = datetime.now().strftime('%Y-%m-%d')

    # Clear the existing data in the collection
    model_data_collection.delete_many({})
    print("Cleared existing data from the database.")

    for ticker in tickers:
        # Check if we have data for this ticker
        existing_data = model_data_collection.find_one({'Ticker': ticker})
        
        if existing_data:
            # If data exists, only fetch the missing dates
            last_date = model_data_collection.find({'Ticker': ticker}).sort('Date', -1).limit(1)[0]['Date']
            start_date = (last_date + timedelta(days=1)).strftime('%Y-%m-%d')
        
        if start_date < end_date:
            new_data = fetch_and_prepare_data(ticker, start_date, end_date)
            
            # Convert DataFrame to list of dictionaries
            data_dict = new_data.to_dict('records')
            
            # Insert new data into MongoDB
            model_data_collection.insert_many(data_dict)
            
            print(f"Updated data for {ticker} from {start_date} to {end_date}")
        else:
            print(f"Data for {ticker} is already up to date")

def ensure_data_is_updated():
    update_database()            

if __name__ == "__main__":
    update_database()