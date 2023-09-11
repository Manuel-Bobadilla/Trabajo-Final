from django.shortcuts import render, get_object_or_404, redirect
from vehicles.models import Vehicle, Volunteer, ActivitieDetailPage
from volunteerings.views import ViewVolunteering
from users.models import User
import json

def VehiclesView(request):
    user = User.objects.get(id = request.user.id)
    volunteer = Volunteer.objects.filter(user = user)

    if not volunteer:
        return render(request, "redirections/user_not_confirmed.html")
    
    vehicles = Vehicle.objects.filter(proprietary = volunteer[0])
    
    return render(request,"vehicles/vehicles.html",
                  {
                      "volunteer":volunteer[0],
                      "vehicles":vehicles,
                  },)

def AddVehicleView(request):
    user = User.objects.get(id = request.user.id)
    volunteer = Volunteer.objects.get(user = user)
    brand = request.POST.get("brand")
    model = request.POST.get("model")
    domain = request.POST.get("domain")
    room = request.POST.get("room")

    vehicle = Vehicle(domain=domain, brand=brand, model=model, proprietary=volunteer, room=room)
    vehicle.save()

    return VehiclesView(request)

def DeleteVehicleView(request):
    Vehicle.objects.get(id=request.POST.get("vehicle_id")).delete()

    return VehiclesView(request)

def SelectVehicleView(request):
    user = User.objects.get(id = request.user.id)
    volunteer = Volunteer.objects.get(user = user)
    activitieAndVehicle = json.loads(request.POST.get("vehicle_option"))
    activitie = get_object_or_404(ActivitieDetailPage, id=activitieAndVehicle["post_id"])
    vehicle = volunteer.vehicles.filter(activitie = activitie)
    if vehicle:
        vehicle[0].activitie = None
        vehicle[0].save(force_update=True)

    if activitieAndVehicle["vehicle"] != "Ninguno":
        vehicle_domain = activitieAndVehicle["vehicle"]
        vehicle = Vehicle.objects.get(domain=vehicle_domain)
        vehicle.activitie = activitie
        vehicle.save(force_update=True)
        
    return ViewVolunteering(request) #cambiar para que determine la url de retorno de manera dinamica


