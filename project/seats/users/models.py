from django.db import models

# Create your models here.


class User(models.Model):
    """User information for Database"""
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
