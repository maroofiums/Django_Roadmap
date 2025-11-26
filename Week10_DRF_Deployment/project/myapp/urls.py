from .views import (
    PostListAPIView,
    PostDetailAPIView
)
from django.urls import path

urlpatterns = [
    path('', PostListAPIView.as_view(),name = "list_post"),
    path('detail/<int:pk>', PostDetailAPIView.as_view(),name = "post_detail"),
]
