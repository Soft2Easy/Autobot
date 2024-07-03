from django.db import models


# Create your models here.

class Car(models.Model):
    vin = models.CharField(max_length=20)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.vin},{self.make},{self.model},{self.year}"
