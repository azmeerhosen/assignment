from django.contrib.auth.models import User
from django.db import models


class Photos:
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_location = models.TextField()
