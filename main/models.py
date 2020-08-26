from django.db import models
from django.contrib.auth.models import User


class UserImage(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images')