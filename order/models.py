from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)
    total = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.surname} - {self.total}"
