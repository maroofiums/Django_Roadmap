import os
import joblib
from django.conf import settings

def load_model():
    model_path = os.path.join(
        settings.BASE_DIR,
        "ml_models",
        "house_price.pkl"
    )
    return joblib.load(model_path)
