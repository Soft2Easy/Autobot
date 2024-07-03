from django.shortcuts import render
from django.http import JsonResponse
from .models import Car
from .serializers import CarSerializer


# Create your views here.
def index(request):
    return render(request, template_name='index.html')


def cars_list(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return JsonResponse(serializer.data, safe=False)
