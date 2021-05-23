from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="photo", default='media/photo/default_photo.png')