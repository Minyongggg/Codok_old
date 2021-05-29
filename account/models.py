from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    GENDER = (
            ('M', 'Male'),
	        ('F', 'Female'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', default=None)
    nickname = models.CharField(max_length=20, default=None)
    gender = models.CharField(max_length=1,choices=GENDER,default='Male')
    gender_open = models.BooleanField(default=True)
    major = models.CharField(max_length=20, default=None)
    studentid = models.CharField(max_length=20, default=None)
    studentid_open = models.BooleanField(default=True)
    introduce = models.TextField(default=None)
    matewant = models.BooleanField(default=False)
    photo = models.ImageField(upload_to="", default='{photo/default_photo.png}')
    portal_id = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nickname

class Lecture(models.Model):
    subject = models.CharField(max_length=100, default=None)
    subnum = models.CharField(max_length=100, primary_key=True, default=None)
    professor = models.CharField(max_length=100, blank=True, null=True)
    subtime = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.subject


class PLR(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="plrs", default=None)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name="plrs", default=None)
