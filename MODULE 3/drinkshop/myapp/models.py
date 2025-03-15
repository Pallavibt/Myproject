from django.db import models

class Drinks(models.Model):
    drink = models.CharField(max_length=200)  # Renamed to `drink`
    price = models.IntegerField()

    def __str__(self):
        return self.drink
    