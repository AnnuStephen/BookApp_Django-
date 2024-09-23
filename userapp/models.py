# from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.db import models

from accounts.models import UserProfile,LoginTable
from adminapp.models import Book

# Create your models here.


class Cart(models.Model):
    # User - model from abstract user - from django.contrib.auth.models import User
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # user=models.OneToOneField(LoginTable,on_delete=models.CASCADE)
    items = models.ManyToManyField(Book)


class CartItem(models.Model):

    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
