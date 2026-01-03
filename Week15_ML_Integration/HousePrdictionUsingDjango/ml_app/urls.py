from django.urls import path
from .views import house_prediction_view, HousePredictionAPI

urlpatterns = [
    path("predict/", house_prediction_view, name="predict-form"),
    path("api/predict/", HousePredictionAPI.as_view(), name="predict-api"),
]
