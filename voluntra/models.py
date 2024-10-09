from django.db import models

# Create your models here.

class PostEvent(models.Model):
    username = models.CharField(max_length = 100)
    nameOfEvent = models.CharField(max_length = 100)
    descOfEvent = models.TextField()
    placeOfEvent = models.CharField(max_length=100)
    dateOfEvent = models.DateField(null=False)
    numOfVol = models.IntegerField()
    minAge = models.IntegerField()
    eventPoster = models.ImageField(upload_to='pics')


class JoinedEvents(models.Model):
    name = models.CharField(max_length=100)
    email = models.TextField()
    age = models.IntegerField()
    gender = models.TextField()