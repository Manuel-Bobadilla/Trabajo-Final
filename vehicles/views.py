from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from vehicles.models import Vehicle, Volunteer, ActivitieDetailPage
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

def AddVehicleView(request):
    user = User.objects.get(id = request.user.id)
    volunteer = Volunteer.objects.get(user = user)
    brand = request.POST.get("brand")
    model = request.POST.get("model")
    domain = request.POST.get("domain")

    vehicle = Vehicle(domain=domain, brand=brand, model=model, proprietary=volunteer)
    vehicle.save()

    return VehiclesView(request)

def DeleteVehicleView(request):
    Vehicle.objects.get(id=request.POST.get("vehicle_id")).delete()

    return VehiclesView(request)

def SelectVehicleView(request):
    user = User.objects.get(id = request.user.id)
    volunteer = Volunteer.objects.get(user = user)
    activitie = get_object_or_404(ActivitieDetailPage, id=request.POST.get("actividad_id"))
    vehicle = volunteer.vehicles.filter(activitie = activitie)
    if vehicle:
        vehicle[0].activitie = None
        vehicle[0].save(force_update=True)

    if request.POST.get("vehicle_option") != "Ninguno":
        vehicle_domain = request.POST.get("vehicle_option")
        vehicle = Vehicle.objects.get(domain=vehicle_domain)
        activitie = get_object_or_404(ActivitieDetailPage, id=request.POST.get("actividad_id"))
        vehicle.activitie = activitie
        vehicle.save(force_update=True)
        
    return VehiclesView(request)
    
# Create your views here.
