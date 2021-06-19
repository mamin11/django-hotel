from django.shortcuts import render
from django.http import HttpResponse
from main.models import Rooms

# Create your views here.
def index(response):
    rooms = Rooms.objects.all()
    return render(response, "main/home.html", {"rooms":rooms})

def room(response, id):
    room = Rooms.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>" %room.room_number)

def about(response):
    rooms = Rooms.objects.get(floor=2)
    return HttpResponse("<h1>Room No: "+rooms.room_number+"</h1><br><h2>Desciption: "+str(rooms.description)+"</h2><br><h2>Floor: "+str(rooms.floor)+"</h2><br><h2>Available: "+str(rooms.isAvailable)+"</h2>")