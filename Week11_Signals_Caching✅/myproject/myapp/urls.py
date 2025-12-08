from django.urls import path
from .views import HomeView,get_popular_posts

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("popular/",get_popular_posts)
]
