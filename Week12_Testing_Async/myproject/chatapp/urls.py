from django.urls import path
from .views import messages_list

urlpatterns = [
    path("messages/", messages_list),
]
