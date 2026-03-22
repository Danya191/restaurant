from django.db import models
from django.contrib.auth.models import User
from menu.models import Dish

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
