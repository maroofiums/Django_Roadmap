import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "ml_models", "house_price.pkl")

model = joblib.load(MODEL_PATH)

def load_model():
    return model
