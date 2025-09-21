from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os

# Initialize FastAPI app
app = FastAPI(title="API Performance Predictor")

# Load model and encoder
import os

model_path = r"C:\Users\ravir\OneDrive\Desktop\ayushproject\api-performance-predictor\model\api_latency_model.pkl"
encoder_path = r"C:\Users\ravir\OneDrive\Desktop\ayushproject\api-performance-predictor\model\endpoint_encoder.pkl"

model = joblib.load(model_path)
encoder = joblib.load(encoder_path)

# Define request body
class PredictRequest(BaseModel):
    endpoint: str
    traffic_rate: float

# Prediction endpoint
@app.post("/predict")
def predict_latency(request: PredictRequest):
    df = pd.DataFrame({
        "endpoint": [request.endpoint],
        "traffic_rate": [request.traffic_rate]
    })
    # Encode endpoint
    df["endpoint_encoded"] = encoder.transform(df["endpoint"])
    # Predict
    prediction = model.predict(df[["traffic_rate", "endpoint_encoded"]])
    return {"predicted_latency_ms": prediction[0]}
