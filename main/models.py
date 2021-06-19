from django.db import models

# Create your models here.
class Rooms(models.Model):
    room_number = models.CharField(max_length=50)
    description = models.TextField()
    floor = models.IntegerField()
    rating = models.IntegerField()
    isAvailable = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return 

