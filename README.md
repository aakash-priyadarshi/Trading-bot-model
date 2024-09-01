# AI Trading Bot - Machine Learning Service

<p align="center">
  <img src="trading-bot.webp" alt="AI Trading Bot ML Logo" width="200"/>
</p>

<p align="center">
  <a href="https://github.com/aakash-priyadarshi/Trading-bot-model/stargazers"><img src="https://img.shields.io/github/stars/aakash-priyadarshi/Trading-bot-model" alt="Stars Badge"/></a>
  <a href="https://github.com/aakash-priyadarshi/Trading-bot-model/network/members"><img src="https://img.shields.io/github/forks/aakash-priyadarshi/Trading-bot-model" alt="Forks Badge"/></a>
  <a href="https://github.com/aakash-priyadarshi/Trading-bot-model/pulls"><img src="https://img.shields.io/github/issues-pr/aakash-priyadarshi/Trading-bot-model" alt="Pull Requests Badge"/></a>
  <a href="https://github.com/aakash-priyadarshi/Trading-bot-model/issues"><img src="https://img.shields.io/github/issues/aakash-priyadarshi/Trading-bot-model" alt="Issues Badge"/></a>
  <a href="https://github.com/aakash-priyadarshi/Trading-bot-model/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/aakash-priyadarshi/Trading-bot-model?color=2b9348"></a>
  <a href="https://github.com/aakash-priyadarshi/Trading-bot-model/blob/master/LICENSE"><img src="https://img.shields.io/github/license/aakash-priyadarshi/Trading-bot-model?color=2b9348" alt="License Badge"/></a>
</p>

<p align="center">
  <img src="https://your-image-hosting-service.com/ai-trading-bot-ml-demo.gif" alt="AI Trading Bot ML Demo" width="600"/>
</p>

> **Note**: The AI Trading Bot logo and demo images used in this README are AI-generated and the exclusive property of Aakash Priyadarshi. These images may not be used, reproduced, or distributed without explicit permission from the owner.

This repository contains the machine learning service component of the AI Trading Bot project. It provides stock price predictions using Azure Machine Learning and handles data preparation for the model.

## 🔗 Related Repositories

This project is split into two main components:

1. **Machine Learning Model (Current Repository)**: 
   Houses the predictive model and data preparation scripts.
   
2. **Frontend and Backend**: 
   Contains the user interface, data visualization, and trading logic.
   GitHub Repository: [ai-trading-bot](https://github.com/aakash-priyadarshi/ai-trading-bot)

For a complete setup of the AI Trading Bot, you'll need to clone and configure both repositories.

## ✨ Features

- Stock price prediction using Azure ML
- Data preparation and feature engineering
- API endpoint for retrieving predictions
- Integration with MongoDB for storing prepared data
- Automated data updates and model retraining

## 🛠️ Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/Azure_ML-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white" alt="Azure ML"/>
  <img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB"/>
  <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
</p>

## 📋 Prerequisites

- Python 3.8 or later
- Azure ML workspace
- MongoDB

## 🚀 Setup

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

## 📁 Project Structure

```
ml_service/
├── data_handler.py
├── predict.py
├── requirements.txt
├── config.json
└── .env
```

## 🔄 API Endpoints

- `/predict` (POST): Get stock price predictions

  Request body:
  ```json
  {
    "symbol": "AAPL",
    "current_price": 150.75,
    "prediction_days": 7
  }
  ```

## 📊 Data Preparation

The `data_handler.py` script fetches historical stock data, calculates technical indicators, and stores the prepared data in MongoDB. Run this script periodically to keep the data up-to-date:

```
python data_handler.py
```

## 🧠 Model Information

The machine learning model used in this service is a Time Series Prophet model trained on Azure ML. The model is loaded from the Azure ML workspace and used for making predictions.

## 🔗 Integration with Frontend/Backend

To integrate this ML service with the frontend and backend components, ensure that the `ML_SERVICE_URL` environment variable in the [ai-trading-bot](https://github.com/aakash-priyadarshi/ai-trading-bot) repository is set to the URL where this Flask application is running.

## 🤝 Contributing

We welcome contributions to the AI Trading Bot project! Please see our [Contributing Guide](CONTRIBUTING.md) for more details on how to get started.

## 💖 Sponsor

If you find this project helpful, consider buying me a coffee!

<a href="https://www.buymeacoffee.com/aakashm30" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

## 📞 Contact

For any queries or suggestions, feel free to reach out:

<a href="https://linktr.ee/aakashPriyadarshi" target="_blank"><img src="https://img.shields.io/badge/linktree-39E09B?style=for-the-badge&logo=linktree&logoColor=white" alt="Linktree"/></a>

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## ©🖼️ Image Usage Rights

The AI-generated images used in this project, including the AI Trading Bot logo and demo images, are the exclusive property of Aakash Priyadarshi. These images are protected by copyright and may not be used, reproduced, modified, or distributed without explicit written permission from the owner.

For inquiries about using these images, please contact Aakash Priyadarshi through the provided Linktree contact link.
