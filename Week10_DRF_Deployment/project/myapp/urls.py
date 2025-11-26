from .views import PostListAPIView
from django.urls import path

urlpatterns = [
    path('', PostListAPIView.as_view(),name = "list_post"),
]
