# AI Trading Bot - Machine Learning Service

This repository contains the machine learning service component of the AI Trading Bot project. It provides stock price predictions using Azure Machine Learning and handles data preparation for the model.

## Related Repositories

This project is split into two main components:

1. **Machine Learning Model (Current Repository)**: 
   Houses the predictive model and data preparation scripts.
   
2. **Frontend and Backend**: 
   Contains the user interface, data visualization, and trading logic.
   GitHub Repository: [ai-trading-bot](https://github.com/aakash-priyadarshi/ai-trading-bot)

For a complete setup of the AI Trading Bot, you'll need to clone and configure both repositories.

## Features

- Stock price prediction using Azure ML
- Data preparation and feature engineering
- API endpoint for retrieving predictions
- Integration with MongoDB for storing prepared data

## Tech Stack

- Python 3.8+
- Flask
- Azure Machine Learning
- pandas, numpy, scikit-learn
- MongoDB

## Prerequisites

- Python 3.8 or later
- Azure ML workspace
- MongoDB

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/aakash-priyadarshi/Trading-bot-model.git
   cd Trading-bot-model
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory and add the following:
   ```
   MONGO_URI=your_mongodb_connection_string
   AZURE_ML_WORKSPACE_NAME=your_workspace_name
   AZURE_ML_SUBSCRIPTION_ID=your_subscription_id
   AZURE_ML_RESOURCE_GROUP=your_resource_group
   ```

5. Configure Azure ML:
   Make sure you have the Azure ML workspace configuration file (`config.json`) in the root directory.

6. Start the Flask application:
   ```
   python predict.py
   ```

The server will start on `http://localhost:5000`.

## Project Structure

```
ml_service/
├── data_handler.py
├── predict.py
├── requirements.txt
├── config.json
└── .env
```

## API Endpoints

- `/predict` (POST): Get stock price predictions

  Request body:
  ```json
  {
    "symbol": "AAPL",
    "current_price": 150.75,
    "prediction_days": 7
  }
  ```

## Data Preparation

The `data_handler.py` script fetches historical stock data, calculates technical indicators, and stores the prepared data in MongoDB. Run this script periodically to keep the data up-to-date:

```
python data_handler.py
```

## Model Information

The machine learning model used in this service is a Time Series Prophet model trained on Azure ML. The model is loaded from the Azure ML workspace and used for making predictions.

## Integration with Frontend/Backend

To integrate this ML service with the frontend and backend components, ensure that the `ML_SERVICE_URL` environment variable in the [ai-trading-bot](https://github.com/aakash-priyadarshi/ai-trading-bot) repository is set to the URL where this Flask application is running.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
