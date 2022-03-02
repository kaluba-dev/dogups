from django.db import models
from users.models import Profile
import uuid
from django_countries.fields import CountryField

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organizer = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    date = models.DateField()
    time = models.TimeField()
    featured_image = models.ImageField(null=True, blank=True, upload_to="meetups/", default="meetups/img-default.jpg")
    description = models.TextField(max_length=500)
    dog_sizes = models.ManyToManyField('DogSize')
    location = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = CountryField()
    attendees = models.ManyToManyField(Profile, related_name="attendees", blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class DogSize(models.Model):
    size = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ['created']
        
    def __str__(self):
        return self.size
