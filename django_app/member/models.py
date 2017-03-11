from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    user_img = models.ImageField(upload_to='user', blank=True)
