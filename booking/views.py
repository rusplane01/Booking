from django.shortcuts import render, redirect
from .models import Room, Booking, Hotel
from django.shortcuts import HttpResponse
from django.conf import settings
User = settings.AUTH_USER_MODEL

def get_room_list(request):
    rooms = Room.objects.all()
    context = {
                "rooms": rooms,
    }
    return render(request, 'booking/room_list.html', context)

def get_room_detail(request, pk):
    room = Room.objects.get(id=pk)
    context = {
                "room": room,
    }
    return render(request, 'booking/room_detail.html', context)

def get_hotel_list(request):
    hotels = Hotel.objects.all()
    context = {
                "hotels": hotels,
    }
    return render(request, 'booking/hotel_list.html', context)

def get_hotel_detail(request, pk):
    hotel = Hotel.objects.get(id=pk)
    context = {
                "hotel": hotel,
    }
    return render(request, 'booking/hotel_detail.html', context)

def index(request):
    return render(request, 'base.html',)     

def booking_detail(request, pk):
    booking = Booking.objects.get(id=pk)
    context = {
        'booking': booking,
    }
    return render(request, 'booking/booking_detail.html', context)

def booking_form(request):
    if request.method == 'GET':
        return render(request, 'booking/booking_form.html')
    else:
        room_number = request.POST.get('room_number')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        try:
            room = Room.objects.get(number=room_number)
        except ValueError: 
            return HttpResponse('Wrong Room Number', status=404)
        except Room.DoesNotExist:
            return HttpResponse("Room does not exist", status=404)
        
        booking = Booking.objects.create(
            room = room,
            user = request.user,
            start_time = start_time,
            end_time = end_time
        )
        return redirect('booking_detail', pk=booking.id)

