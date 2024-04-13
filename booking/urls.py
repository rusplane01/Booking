from django.urls import path, include
from .views import get_room_list, index, get_room_detail, booking_detail, booking_form

urlpatterns = ([
    path('room_list', get_room_list, name='room_list'),
    path('', index, name='index'),
    path('<int:pk>/', get_room_detail, name='room_detail'),
    path('booking_detail/<int:pk>/', booking_detail, name='booking_detail'),
    path('booking/', booking_form, name='booking_form'),
])