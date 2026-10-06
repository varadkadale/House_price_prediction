from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(
    title="House Price Prediction API",
    description="API for predicting house prices using Machine Learning",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

model = joblib.load("model/house_price_model.pkl")


class HouseData(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    stories: int
    parking: int
    age: int
    location: str


@app.get("/")
def home():
    return {
        "message": "House Price Prediction API is running successfully"
    }


@app.post("/predict")
def predict_house_price(data: HouseData):

    input_data = pd.DataFrame([{
        "area": data.area,
        "bedrooms": data.bedrooms,
        "bathrooms": data.bathrooms,
        "stories": data.stories,
        "parking": data.parking,
        "age": data.age,
        "location": data.location
    }])

    prediction = model.predict(input_data)[0]

    return {
        "predicted_price": round(float(prediction), 2)
    }