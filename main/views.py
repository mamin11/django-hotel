from django.shortcuts import render
from django.http import HttpResponse
from main.models import Rooms

# Create your views here.
def index(response):
    rooms = Rooms.objects.all()
    return render(response, "main/home.html", {"rooms":rooms})

def room(response, id):
    room = Rooms.objects.get(id=id)
    return render(response, "main/singleRoom.html", {"room":room})

def about(response):
    return render(response, "main/about.html")

def rooms(response):
    rooms = Rooms.objects.all()
    return render(response, "main/rooms.html", {"rooms":rooms})