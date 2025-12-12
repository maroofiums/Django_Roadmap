from django.shortcuts import render
from .models import Room, Message

def room_list(request):
    rooms = Room.objects.all()
    return render(request, "room_list.html", {"rooms": rooms})


def room(request, room_name):
    room_obj = Room.objects.get(name=room_name)
    messages = room_obj.messages.order_by("timestamp")
    return render(request, "chat_room.html", {
        "room_name": room_name,
        "messages": messages
    })
