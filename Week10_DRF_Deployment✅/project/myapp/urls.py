from .views import PostViewSet
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
]