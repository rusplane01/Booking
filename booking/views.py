from django.shortcuts import render, redirect
from .models import Room, Booking
from django.shortcuts import HttpResponse

def get_room_list(request):
    rooms = Room.objects.all()
    context = {
                "rooms": rooms,
    }
    return render(request, 'room_list.html', context)

def index(request):
    return render(request, 'base.html',) 

def get_room_detail(request, pk):
    room = Room.objects.get(id=pk)
    context = {
                "room": room,
    }
    return render(request, 'room_detail.html', context)    

def booking_detail(request, pk):
    booking = Booking.objects.get(id=pk)
    context = {
        'booking': booking,
    }
    return render(request, 'booking_detail.html', context)

def booking_form(request):
    if request.method == 'GET':
        return render(request, 'booking_form.html')
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

