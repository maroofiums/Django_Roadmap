from django.urls import path
from .views import house_prediction_view, house_prediction_api_view

urlpatterns = [
    path("", house_prediction_view, name="predict-form"),
    path("api/predict/", house_prediction_api_view, name="predict-api"),
]
