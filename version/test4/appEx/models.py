from django.db import models
from django import forms


# Create your models here.
class Acc(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=1000)
    balance=models.FloatField()

class Invested(models.Model):
    name=models.CharField(max_length=30)
    invested=models.CharField(max_length=30)
    shares=models.FloatField()

class FavoriteStock(models.Model):
    name=models.CharField(max_length=30)
    favorite=models.CharField(max_length=30)