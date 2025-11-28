from .views import (
#     PostListAPIView,
#     PostDetailAPIView,
#     PostCreateAPI,
#     PostUpdateAPI,
#     PostDeleteAPI
    PostViewSet
 )
from django.urls import path,include

# urlpatterns = [
#     path('', PostListAPIView.as_view(),name = "list_post"),
#     path('detail/<int:pk>', PostDetailAPIView.as_view(),name = "post_detail"),
#     path('new/', PostCreateAPI.as_view(),name = "create_post"),
#     path('update/<int:pk>', PostUpdateAPI.as_view(),name = "update_post"),
#     path('delete/<int:pk>', PostDeleteAPI.as_view(),name = "delete_post"),
# ]

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
]