from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.



class Products(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=80, blank=False)
    image = models.TextField(max_length=400, blank=False)
    categoryId = models.CharField(max_length=20, blank=False)
    materia = models.CharField(max_length=50, blank=False)
    price = models.FloatField(null=False)
    stock = models.IntegerField(null=False)


# class User(AbstractUser):
#     legajo = models.CharField(max_length=12, blank=False)
#     dni = models.IntegerField( null=False)
#     phone = models.IntegerField(null=False)
class User(AbstractUser):
    legajo = models.CharField(max_length=12, blank=False)
    dni = models.BigIntegerField(null=False)
    phone = models.BigIntegerField(null=False)


class Orders(models.Model):
    user_id = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='user')
    total_price = models.FloatField(null=False)
    date = models.DateField(null=False, auto_now_add=True)
    # state = models.IntegerField(default=False, max_length=2)
    user_mail = models.CharField(default=False, max_length=70)
    state = models.CharField(default=False, max_length=30)

class Order_Detail(models.Model):
    order_id = models.ForeignKey(Orders, null=False, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, null=False, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    product_title = models.CharField(max_length=50, blank=False)
    anillado = models.IntegerField(null=False)