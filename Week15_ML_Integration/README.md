

# 🟦 Week 15: Django + ML Integration 

> **Goal:** Train model → Save → Load in Django → Serve predictions via Form/API → Optional AJAX frontend.

---

## **Day 1 — Train ML Model**

### Steps:

1. Pick a simple dataset (House Price, Energy Prediction, etc.)
2. Train a model:

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
```

3. Evaluate quickly:

```python
score = model.score(X_test, y_test)
print("Accuracy:", score)
```

💡 **Tip:** Start simple → LinearRegression / DecisionTree. Complexity later.

---

## **Day 2 — Save Model**

### Steps:

1. Create folder: `ml_models/`
2. Save using `joblib`:

```python
import joblib
joblib.dump(model, "ml_models/house_price.pkl")
```

💡 **Tip:** Never save inside app folder; keep models separate.

---

## **Day 3 — Load Model in Django**

### Steps:

1. Load **once globally** (not per request):

```python
# ml_models/loader.py
import joblib
model = joblib.load("ml_models/house_price.pkl")
```

2. Import in views:

```python
from ml_models.loader import model

def predict_price(area, rooms):
    return model.predict([[area, rooms]])[0]
```

💡 **Avoid:** Reloading model per request → slow performance.

---

## **Day 4 — Create Form / API Endpoint**

### Form Example:

```python
# forms.py
from django import forms

class PredictionForm(forms.Form):
    area = forms.FloatField()
    rooms = forms.IntegerField()
```

### View Example:

```python
# views.py
from django.shortcuts import render
from .forms import PredictionForm
from ml_models.loader import model

def predict_view(request):
    price = None
    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            area = form.cleaned_data['area']
            rooms = form.cleaned_data['rooms']
            price = model.predict([[area, rooms]])[0]
    else:
        form = PredictionForm()
    return render(request, "predict.html", {"form": form, "price": price})
```

---

## **Day 5 — API Endpoint (DRF)**

```python
# serializers.py
from rest_framework import serializers

class PredictionSerializer(serializers.Serializer):
    area = serializers.FloatField()
    rooms = serializers.IntegerField()
    price = serializers.FloatField(read_only=True)
```

```python
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PredictionSerializer
from ml_models.loader import model

class PredictionAPI(APIView):
    def post(self, request):
        serializer = PredictionSerializer(data=request.data)
        if serializer.is_valid():
            area = serializer.validated_data['area']
            rooms = serializer.validated_data['rooms']
            serializer.validated_data['price'] = model.predict([[area, rooms]])[0]
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=400)
```

---

## **Day 6 — Optional AJAX Frontend**

### Steps:

1. Use `<form id="predictForm">`
2. JS fetch API to POST data to `/api/predict/`
3. Update result div dynamically → no page reload

💡 **Tip:** Smooth UX = recruiter + user friendly.

---

## **Day 7 — Mini Project Integration**

### Mini Project: **House Price Predictor App**

**Features:**

* Input via form + API
* Model prediction
* Validation + error handling
* Optional AJAX frontend
* Keep ML models in `ml_models/`
* Logs / cache if needed

**Flow:**

```
User input → Django form/API → ML model → Prediction → Render on UI
```

---

### ✅ Final Notes for Week 15

1. Keep models **separate** from app code (`ml_models/`)
2. **Load once globally** → performance
3. Add **basic error handling + validation**
4. AJAX optional, but recommended for smooth UX
5. Post Week 15 → Tum ready ho real ML-backed Django apps ke liye
