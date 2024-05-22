from django.urls import path, include
from .views import *

urlpatterns = ([
    path('room_list', get_room_list, name='room_list'),
    path('', index, name='index'),
    path('<int:pk>/', get_room_detail, name='room_detail'),
    path('booking_detail/<int:pk>/', booking_detail, name='booking_detail'),
    path('booking/', booking_form, name='booking_form'),
    path('hotel_list/', get_hotel_list, name='hotel_list'),
    path('hotel/<int:pk>/', get_hotel_detail, name='hotel_detail'),
])