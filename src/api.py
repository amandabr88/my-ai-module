from fastapi import FastAPI
from .inference import predict

app = FastAPI(title="My AI Module API")

@app.get("/")
def read_root():
    return {"message": "AI Module API is running"}

@app.post("/predict")
def get_prediction(features: dict):
    prediction = predict(features)
    return {"prediction": prediction}
