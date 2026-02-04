# Customer Churn Prediction & Analytics Platform

A comprehensive machine learning solution for predicting customer churn with interactive dashboard and REST API.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28-orange)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌟 Features

### 1. **Machine Learning Pipeline**
- Logistic Regression model with Optuna hyperparameter optimization
- Feature preprocessing and SMOTE for handling class imbalance
- Cross-validation with Stratified K-Fold
- Model persistence with pickle

### 2. **Interactive Dashboard** (3 Pages)
- **📊 Analytics Dashboard**: Customer demographics and churn analysis
- **🔮 Prediction Interface**: Real-time churn prediction form
- **📈 Model Insights**: Performance metrics and feature importance

### 3. **REST API Service**
- FastAPI backend with automatic OpenAPI documentation
- Type-safe request/response schemas using Pydantic
- CORS enabled for frontend integration
- Health check endpoints

### 4. **Modern Frontend**
- Streamlit-based web interface
- Responsive design with custom color scheme
- Real-time predictions with confidence scores
- Intuitive user experience

