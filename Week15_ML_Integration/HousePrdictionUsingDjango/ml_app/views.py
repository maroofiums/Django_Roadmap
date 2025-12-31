# ml_app/views.py

from django.http import JsonResponse
from HousePrdictionUsingDjango.loaders import model

def predict_price(request):
    area = int(request.GET.get("area", 1000))
    rooms = int(request.GET.get("rooms", 2))

    prediction = model.predict([[area, rooms]])[0]

    return JsonResponse({
        "area": area,
        "rooms": rooms,
        "predicted_price": round(prediction, 2)
    })
