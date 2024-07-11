from django.db import models


# Create your models here.

class Car(models.Model):
    vin = models.CharField(max_length=20)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.vin},{self.make},{self.model},{self.year}"


class ServicePro(models.Model):
    name = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name},{self.cellphone},{self.email}"


class ServiceRec(models.Model):
    date = models.DateTimeField()
    type_of_service = models.CharField(max_length=100)
    service_provider = models.ForeignKey(ServicePro, related_name='service_provider', on_delete=models.CASCADE)
    note = models.CharField(max_length=200)
    car = models.ForeignKey(Car, related_name='service_record', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date},{self.type_of_service},{self.service_provider},{self.note}"

