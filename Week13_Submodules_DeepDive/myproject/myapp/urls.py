from .views import upload
from django.urls import path

urlpatterns = [
    path('upload/', upload, name='upload_document'),
]