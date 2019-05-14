from django.shortcuts import render
from dr.models import Room, Reservation, User

# Create your views here.

def index(request):
    """View function for home page of system website"""

    #Generate counts of some of the main objects
    num_rooms = Room.objects.all().count()
    num_reservations = Reservation.objects.all().count()
    num_users = User.objects.all().count()

    # Available rooms ( status = 'a')
    num_rooms_available = Room.objects.filter(status='a').count()

    context = {
        'num_rooms' : num_rooms,
        'num_reservations': num_reservations,
        'num_users' : num_users,
        'num_rooms_available' : num_rooms_available, 
    }

    return render(request, 'index.html', context=context)