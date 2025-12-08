from django.http import JsonResponse
from .models import ChatMessage

def messages_list(request):
    data = list(ChatMessage.objects.values())
    return JsonResponse({"messages": data})
