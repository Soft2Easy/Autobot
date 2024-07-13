from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
def index(request):
    return render(request, template_name='index.html')


#Car Methods
@api_view(['GET', 'POST'])
def cars_list(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def car_detail(request, id):
    try:
        car = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarSerializer(car)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Service Proviers

@api_view(['POST', 'GET'])
def service_provider_list(request):
    if request.method == 'GET':
        providers = ServicePro.objects.all()
        provider_serializers = ServiceProviderSerializer(providers, many=True)
        return Response(provider_serializers.data)
    if request.method == 'POST':
        provider_serializer = ServiceProviderSerializer(data=request.data)
        if provider_serializer.is_valid():
            provider_serializer.save()
            return Response(status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def service_provider_detail(request, id):
    try:
        service_provider = ServicePro.objects.get(id)

    except ServicePro.DoNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        service_pro = ServiceProviderSerializer(service_provider)
        return Response(service_pro.data)
    elif request.method == 'PUT':
        provider_serializer = ServiceProviderSerializer(service_provider, data=request.data)
        if provider_serializer.is_valid():
            provider_serializer.save()
            return Response(provider_serializer.data)
        return Response(provider_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        service_provider.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#SERVICE RECORDS
@api_view(['GET', 'POST'])
def service_record_list(request):
    if request.method == 'GET':
        service_records = ServiceRec.objects.all()
        records_serializer = ServiceRecordSerializer(service_records, many=True)
        return Response(records_serializer.data)
    if request.method == 'POST':
        service_record = ServiceRecordSerializer(data=request.data)
        if service_record.is_valid():
            service_record.save()
            return Response(status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def service_records_details(request, id):
    try:
        record = ServiceRec.objects.get(pk=id)
    except ServiceRec.DoNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        service_recs = ServiceRecordSerializer(record)
        return Response(service_recs.data)

    elif request.method == 'PUT':
        record_serializer = ServiceRecordSerializer(record, data=request.data)
        if record_serializer.is_valid():
            record_serializer.save()
            return Response(record_serializer.data)
        return Response(record_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        record.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
