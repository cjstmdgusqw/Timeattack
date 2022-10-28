from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    name = models.CharField(max_length = 10)
    

class Article(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length= 100)
    content = models.TextField()