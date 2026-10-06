# 🏠 House Price Prediction Using Machine Learning

## 📌 Project Overview

House Price Prediction is a Machine Learning based web application that predicts the estimated price of a house based on various property features.

The system takes property details such as area, bedrooms, bathrooms, number of floors, parking spaces, property age, and location as input and predicts the estimated house price.

The project uses a Machine Learning model for prediction, FastAPI for the backend API, and HTML, CSS, and JavaScript for the frontend.

---

## 🎯 Objective

The main objective of this project is to develop a Machine Learning based system that can predict house prices using important property features.

The system provides a simple web interface where users can enter property information and get the predicted house price.

---

## ✨ Features

- House price prediction
- Machine Learning based prediction
- FastAPI backend
- HTML, CSS and JavaScript frontend
- Data preprocessing
- One Hot Encoding for location
- Linear Regression model
- Model evaluation
- Saved Machine Learning model
- REST API
- Swagger API documentation
- User-friendly prediction form

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Machine Learning

- Pandas
- NumPy
- Scikit-learn
- Joblib

### Backend

- FastAPI
- Uvicorn

### Frontend

- HTML
- CSS
- JavaScript

---

## 📊 Dataset

The project uses a dataset containing house property information.

### Dataset Features

| Feature | Description |
|---|---|
| area | House area in square feet |
| bedrooms | Number of bedrooms |
| bathrooms | Number of bathrooms |
| stories | Number of floors |
| parking | Number of parking spaces |
| age | Property age in years |
| location | House location |
| price | House price |

The dataset contains 500 records and is prepared for educational Machine Learning purposes.

---

## 🤖 Machine Learning Model

The project uses **Linear Regression** to predict house prices.

The dataset is divided into:

- 80% Training Data
- 20% Testing Data

The location feature is categorical, so **One Hot Encoding** is used to convert it into numerical form.

The complete preprocessing and Machine Learning model are combined into a Pipeline and saved using Joblib.

---

## 🔄 Project Workflow

```text
User Input
    ↓
HTML/CSS/JavaScript Frontend
    ↓
FastAPI Backend
    ↓
Data Preprocessing
    ↓
Machine Learning Model
    ↓
House Price Prediction
    ↓
Result Displayed on Website
