from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cars', views.cars_list, name='cars_list'),
    path('cars/<int:id>', views.car_detail),
    path('serviceProviders', views.service_provider_list, name='service_provider_list'),
    path('home', views.home_page, name='homepage'),
    path('car', views.car_page, name='car'),
    path('registration', views.registration_page, name='registration'),
    path('dashboard', views.dashboard_page, name='dashboard'),
    path('service-provider', views.service_provider, name='service provider'),
    path('service-details', views.service_details, name='service details'),

]
