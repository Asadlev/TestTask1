from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=29)
    date_started = models.DateTimeField(auto_now_add=True)
    cost = models.DecimalField(max_digits=11, decimal_places=2)


class Lessons(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    video = models.URLField()


class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    users_min = models.IntegerField()
    users_max = models.IntegerField()
    members = models.ManyToManyField(User)

