from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cars', views.cars_list, name='cars_list'),
    path('cars/<int:id>', views.car_detail)
]
