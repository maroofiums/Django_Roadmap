# from .views import upload
# from django.urls import path

# urlpatterns = [
#     path('upload/', upload, name='upload_document'),
# ]

from django.urls import path
from .views import post_list,send_test_email

urlpatterns = [
    path('', post_list, name='post_list'),
    path('send-email/', send_test_email, name='send_email'),
]
