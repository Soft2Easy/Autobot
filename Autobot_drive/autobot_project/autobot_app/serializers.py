from rest_framework import serializers
from .models import *


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'vin', 'make', 'model', 'year']


class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePro
        fields = ['id', 'name', 'cellphone', 'email']


class ServiceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRec
        fields = ['id', 'date', 'type_of_service', 'service_provider', 'note', 'car']

