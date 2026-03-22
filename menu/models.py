from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    weight = models.CharField(max_length=50)
    image = models.ImageField(upload_to='dishes/')
    

    def __str__(self):
        return self.name