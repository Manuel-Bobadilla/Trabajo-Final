from django.shortcuts import render
from django.views.generic import ListView, DetailView
from vehicles.models import Vehicle, Volunteer
from users.models import User

def VehiclesView(request):
    user = User.objects.get(id = request.user.id)
    volunteer = Volunteer.objects.get(user = user)
    vehicles = Vehicle.objects.filter(proprietary = volunteer)

    return render(request,"vehicles/vehicles.html",
                  {
                      "volunteer":volunteer,
                      "vehicles":vehicles,
                  },)
    
# Create your views here.
