from django.shortcuts import render
from passengerApp.models import Passenger

# Create your views here.
def passengerDetails(request):
    passengers = Passenger.objects.all
    passenger_dict = {'passengers':passengers}
    return render(request, 'passengerApp/passengers.html', passenger_dict)

