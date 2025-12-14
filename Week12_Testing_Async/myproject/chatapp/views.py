from django.shortcuts import render, get_object_or_404
from .models import Room

def home(request):
    rooms = Room.objects.all()
    return render(request, "home.html", {"rooms": rooms})

def room_detail(request, room_name):
    room = get_object_or_404(Room, name=room_name)
    return render(request, "room.html", {"room": room})
