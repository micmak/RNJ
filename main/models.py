from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete


class UserImage(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images')


def delete_image_file(sender, instance, **kwargs):
    instance.image.storage.delete(instance.image.name)

post_delete.connect(delete_image_file, sender=UserImage)