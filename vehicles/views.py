from django.shortcuts import render, get_object_or_404, redirect
from vehicles.models import Vehicle, Volunteer, ActivitieDetailPage
from volunteerings.views import ViewVolunteering
from users.models import User
from django.http import QueryDict
import json

def VehiclesView(request):
    user = User.objects.get(id = request.user.id)
    volunteer = Volunteer.objects.filter(user = user, validated = True)

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

    url_destino = f'/vehiculos/'

    return redirect(url_destino)

def ModifyVehicleView(request):
    print("holaaaaaaa")
    vehicle = Vehicle.objects.get(id=request.POST.get("vehicle_id"))

    print("holaaaaaaa")
    print(request.POST)
    #vehicle.brand = request.POST.get("brand")
    #vehicle.model = request.POST.get("model")
    #vehicle.domain = request.POST.get("domain")
    #vehicle.room = request.POST.get("room")

    #vehicle.save()

    url_destino = f'/vehiculos/'

    return redirect(url_destino)

def DeleteVehicleView(request):
    Vehicle.objects.get(id=request.POST.get("vehicle_id")).delete()

    url_destino = f'/vehiculos/'

    return redirect(url_destino)

def SelectVehicleView(request):
    volunteer = Volunteer.objects.get(user__id = request.user.id)
    activitieAndVehicle = json.loads(request.POST.get("vehicle_option"))
    activitie = get_object_or_404(ActivitieDetailPage, id=activitieAndVehicle["post_id"])
    vehicle = volunteer.vehicles.filter(activitie = activitie)
    if vehicle:
        vehicle[0].activitie.remove(activitie)
        vehicle[0].save(force_update=True)
        if vehicle[0].domain == "Pasajero":
            vehicle[0].delete()

    if activitieAndVehicle["vehicle"] != "Ninguno" and activitieAndVehicle["vehicle"] != "Pasajero":
        vehicle_domain = activitieAndVehicle["vehicle"]
        vehicle = Vehicle.objects.get(domain=vehicle_domain, proprietary=volunteer)
        vehicle.activitie.add(activitie)
        vehicle.save(force_update=True)

    if activitieAndVehicle["vehicle"] == "Pasajero":
        vehicle = Vehicle(domain="Pasajero", brand="", model="", proprietary=volunteer)
        vehicle.save()
        vehicle.activitie.add(activitie)
        vehicle.save(force_update=True)

    mutable_get = request.GET.copy()
    mutable_get['volunteering_id'] = request.POST.get("volunteering_id")
    request.GET = QueryDict(mutable_get.urlencode(), mutable=False)
        
    url_destino = f'/voluntariado/?volunteering_id={request.POST.get("volunteering_id")}'

    return redirect(url_destino)


