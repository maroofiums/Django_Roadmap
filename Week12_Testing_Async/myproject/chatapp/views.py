from django.shortcuts import render
from .models import Message

def chat_home(request):
    messages = Message.objects.order_by("-timestamp")[:25]  # latest 25
    messages = reversed(messages)  # old → new order
    return render(request, "chat_home.html", {"messages": messages})
