import pandas as pd
import numpy as np
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("data/house_prices.csv")

print("Dataset Loaded Successfully")
print("Dataset Shape:", df.shape)

df = df.drop_duplicates()

print("After Removing Duplicates:", df.shape)

X = df.drop("price", axis=1)
y = df["price"]

numeric_features = [
    "area",
    "bedrooms",
    "bathrooms",
    "stories",
    "parking",
    "age"
]

categorical_features = [
    "location"
]

preprocessor = ColumnTransformer(
    transformers=[
        ("numeric", "passthrough", numeric_features),
        ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("regressor", LinearRegression())
    ]
)

print("\nTraining Model...")

model.fit(X_train, y_train)

print("Model Training Completed")

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)

print("\n==============================")
print("MODEL EVALUATION")
print("==============================")

print("Mean Absolute Error (MAE):", round(mae, 2))

print("Mean Squared Error (MSE):", round(mse, 2))

print("Root Mean Squared Error (RMSE):", round(rmse, 2))

print("R2 Score:", round(r2, 4))

print("==============================")

os.makedirs("model", exist_ok=True)

joblib.dump(
    model,
    "model/house_price_model.pkl"
)

print("\nModel saved successfully!")
print("Location: model/house_price_model.pkl")