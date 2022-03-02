from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django_countries.fields import CountryField
import uuid


# Gender choices
FEMALE = 'Female'
MALE = 'Male'
OTHER = 'Other'

USER_GENDER_CHOICES = [
    (FEMALE, 'Female'),
    (MALE, 'Male'),
    (OTHER, 'Non binary/None of these choices'),
]

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    country = CountryField()
    account_creation = models.DateField(auto_now=True, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to="profiles/", default="profiles/user-default.png")
    user_gender = models.CharField(max_length=32, null=True, blank=True, choices=USER_GENDER_CHOICES)
    user_age = models.IntegerField(null=True, blank=True)
    bio = models.TextField(max_length=300, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.username
