from .views import upload_document
from django.urls import path

urlpatterns = [
    path('upload/', upload_document, name='upload_document'),
]