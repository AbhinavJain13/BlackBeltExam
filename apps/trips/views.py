from django.shortcuts import render, redirect, HttpResponse
from ..login.models import User
from ..trips.models import Trip
from django.contrib import messages

def index(request):
    context= {
    'trips' : Trip.objects.all()
    }
    return render(request, 'trips/trip.html')

def showaddpage(request):
    return render(request, 'trips/add.html')

def add(request):
    if request.method == 'POST':
        param ={
        'd_name' : request.POST['d_name'],
        'descrip': request.POST['descrip'],
        'f_date': request.POST['f_date'],
        't_date': request.POST['t_date']
        }
        result = Trip.objects.valid_add(param)
        print "Trip table is there"
        if result[0] == False:
            print_messages(request, result[1])
            return render(request, 'trips/add.html')

        return redirect('trips:index')
    return redirect('trips:index')
