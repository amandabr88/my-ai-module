from .model import load_model
from .preprocess import preprocess_data
import pandas as pd

def predict(input_data: dict):
    """Takes a dict of features, preprocesses, and predicts."""
    df = pd.DataFrame([input_data])
    df = preprocess_data(df)
    model = load_model()
    prediction = model.predict(df)
    return prediction.tolist()
