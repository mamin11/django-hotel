from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("rooms/", views.rooms, name="rooms"),
    path("help/", views.room, name="help"),
    path("contact/", views.room, name="contact"),
    path("room/<int:id>/", views.room, name="viewRoom"),
]
