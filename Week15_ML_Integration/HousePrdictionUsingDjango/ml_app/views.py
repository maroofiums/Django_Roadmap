from django.shortcuts import render

from HousePrdictionUsingDjango.loaders import load_model

def predict_price(area, rooms):
    model = load_model()
    prediction = model.predict([[area, rooms]])
    return prediction[0]

