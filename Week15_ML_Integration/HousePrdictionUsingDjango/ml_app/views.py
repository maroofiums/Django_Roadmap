from django.shortcuts import render
from .forms import HousePredictionForm
from HousePrdictionUsingDjango.loaders import load_model

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import HousePredictionSerializer

model = load_model()

# HTML FORM VIEW
def house_prediction_view(request):
    prediction = None

    if request.method == "POST":
        form = HousePredictionForm(request.POST)
        if form.is_valid():
            area = form.cleaned_data["area"]
            bedrooms = form.cleaned_data["bedrooms"]

            prediction = model.predict([[area, bedrooms]])[0]
    else:
        form = HousePredictionForm()

    return render(
        request,
        "ml_app/house_prediction.html",
        {
            "form": form,
            "prediction": round(prediction, 2) if prediction else None
        }
    )

# API VIEW
@api_view(["GET", "POST"])
def house_prediction_api_view(request):
    if request.method == "GET":
        return Response({
            "message": "Use POST with area & bedrooms"
        })
    serializer = HousePredictionSerializer(data=request.data)

    if serializer.is_valid():
        area = serializer.validated_data["area"]
        bedrooms = serializer.validated_data["bedrooms"]

        prediction = model.predict([[area, bedrooms]])[0]

        return Response({
            "area": area,
            "bedrooms": bedrooms,
            "predicted_price": round(prediction, 2)
        })

    return Response(serializer.errors, status=400)
