from django.contrib import admin
from .models import Car, ServiceRec, ServicePro

# Register your models here.

admin.site.register(Car)
admin.site.register(ServiceRec)
admin.site.register(ServicePro)
