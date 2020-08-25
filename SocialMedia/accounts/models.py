from django.db import models
from django.contrib import auth

# Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin, models.Model):
    profile_pic = models.ImageField(upload_to='user_app/profile_pics',blank=True)

    def __str__(self):
        return "@{}".format(self.username)
