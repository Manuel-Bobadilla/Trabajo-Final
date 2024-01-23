from django.shortcuts import render, get_object_or_404, redirect
from volunteerings.models import Volunteering
from activitie.models import ActivitieDetailPage
from attendances.models import Attendance
from restart.models import Restart
from users.models import Volunteer, User
from django.db.models import Q
from django.http import QueryDict
from django.core.exceptions import ObjectDoesNotExist
import datetime

def Volunteerings(request):
    volunteerings = Volunteering.objects.all()
    volunteer = None

    if request.user.id:
        user = User.objects.get(id = request.user.id)
        volunteer = Volunteer.objects.get(user = user)

    return render(request, "volunteerings/volunteerings.html",{"volunteerings":volunteerings,
                                                               "volunteer": volunteer,})

def ViewVolunteering(request):
    volunteering = Volunteering.objects.get(id = request.GET.get("volunteering_id"))
    posts = ActivitieDetailPage.objects.filter(volunteering=volunteering)
    current_date = datetime.date.today()
    inscripted = False
    if request.user.id:
        user = User.objects.get(id=request.user.id)
        volunteer = Volunteer.objects.filter(user = user)
        volunteeringsOfVolunteer = Volunteering.objects.filter(volunteers__in = volunteer)
        if volunteering in volunteeringsOfVolunteer:
                inscripted = True
        if volunteer[0].validated:
            activities = ActivitieDetailPage.objects.filter(volunteers = volunteer[0])
            vehicles = volunteer[0].vehicles.all()
            activities = activities
            volunteer = volunteer[0]
            return render(request, "activitie/activitie_listing_page.html",{
                    "posts":posts,
                    "current_date":current_date,
                    "vehicles":vehicles,
                    "activities":activities,
                    "volunteer":volunteer,
                    "inscripted":inscripted,
                    "volunteering":volunteering,
                    "day_number": current_date.weekday(),
            })
    volunteer = None
    return render(request, "activitie/activitie_listing_page.html",{
         "posts":posts,
         "current_date":current_date,
         "volunteer":volunteer,
         "volunteering":volunteering,
    })

def ViewVolunteersVolunteeing(request):
    #verificar que quien acceda sea un coordinador
    try:
        coordinator = Volunteer.objects.get(Q(user__id=request.user.id) & Q(user__is_superuser=True))
    except ObjectDoesNotExist:
        coordinator = Volunteer.objects.get(Q(user__id=request.user.id) & Q(coordinador=True) & Q(volunteering__id=request.GET.get("volunteering_id")))
    volunteering = Volunteering.objects.get(id=request.GET.get("volunteering_id"))
    volunteeringVolunteers = None
    restOfVolunteers = None
    coordinadores = "false"

    if 'coordinadores' in request.GET:
        if request.GET.get("coordinadores") == "false":
            volunteeringVolunteers = Volunteer.objects.filter(volunteering=volunteering, validated = True).order_by("user__last_name")
            restOfVolunteers = Volunteer.objects.exclude(Q(volunteering=volunteering) | Q(validated=False)).order_by("user__last_name")
            coordinadores = "true"
        else:
            volunteeringVolunteers = Volunteer.objects.filter(volunteering=volunteering, validated = True, coordinador = True).order_by("user__last_name")
            restOfVolunteers = Volunteer.objects.exclude(Q(volunteering=volunteering) | Q(Q(validated=False) | Q(coordinador = False))).order_by("user__last_name")
    else:
        volunteeringVolunteers = Volunteer.objects.filter(volunteering=volunteering, validated = True).order_by("user__last_name")
        restOfVolunteers = Volunteer.objects.exclude(Q(volunteering=volunteering) | Q(validated=False)).order_by("user__last_name")
        coordinadores = "true"

        

    return render(request, "volunteerings/volunteers.html",{
         "volunteering":volunteering,
         "volunteeringVolunteers":volunteeringVolunteers,
         "restOfVolunteers":restOfVolunteers,
         "coordinadores":coordinadores,
    })

def InscriptionVolunteering(request):
    #verificar que quien acceda sea un coordinador
    try:
        coordinator = Volunteer.objects.get(Q(user__id=request.user.id) & Q(user__is_superuser=True))
    except ObjectDoesNotExist:
        coordinator = Volunteer.objects.get(Q(user__id=request.user.id) & Q(coordinador=True) & Q(volunteering__id=request.POST.get("volunteering_id")))
    coordinadores = request.POST.get("coordinadores")
    volunteersInscriptedId = set()
    volunteersInscripted = None
    volunteering = None
    volunteeringVolunteers = None

    for attendance in request.POST:
        if attendance != "volunteering_id" and attendance != "csrfmiddlewaretoken" and attendance != "coordinadores":
            volunteersInscriptedId.add(attendance)
    volunteersInscriptedIdList = list(volunteersInscriptedId)

    if coordinadores == "true":
        volunteersInscripted = Volunteer.objects.filter(id__in = volunteersInscriptedIdList)
        volunteering = get_object_or_404(Volunteering, id=request.POST.get("volunteering_id"))
        volunteeringVolunteers = Volunteer.objects.filter(volunteering = volunteering)
    else:
        volunteersInscripted = Volunteer.objects.filter(id__in = volunteersInscriptedIdList, coordinador = True)
        volunteering = get_object_or_404(Volunteering, id=request.POST.get("volunteering_id"))
        volunteeringVolunteers = Volunteer.objects.filter(volunteering = volunteering, coordinador = True)

    for volunteer in volunteeringVolunteers:
        if volunteer.id not in volunteersInscriptedIdList:
            activities = ActivitieDetailPage.objects.filter(volunteering = volunteering)
            for activity in activities:
                activity.volunteers.remove(volunteer)
                vehicle = volunteer.vehicles.filter(activitie = activity)
                if vehicle:
                    vehicle[0].activitie.remove(activity)
                    vehicle[0].save(force_update=True)

            volunteering.volunteers.remove(volunteer)
    
    for volunteer in volunteersInscripted:
        if not volunteering.volunteers.filter(id=volunteer.id).exists():
            volunteering.volunteers.add(volunteer)

    mutable_get = request.GET.copy()
    mutable_get['volunteering_id'] = request.POST.get("volunteering_id")
    request.GET = QueryDict(mutable_get.urlencode(), mutable=False)

    url_destino = f'/voluntariados/'

    return redirect(url_destino)

def AttendanceVolunteering(request):
    #verificar que quien acceda sea un coordinador
    print("inicio funcion!!!!")
    try:
        coordinator = Volunteer.objects.get(Q(user__id=request.user.id) & Q(user__is_superuser=True))
    except ObjectDoesNotExist:
        coordinator = Volunteer.objects.get(Q(user__id=request.user.id) & Q(coordinador=True) & Q(volunteering__id=request.GET.get("volunteering_id")))
    print("Validó voluntarioooo!!!!")
    print("id voluntariado: ")
    print(request.GET.get("volunteering_id"))
    volunteering = Volunteering.objects.filter(id = request.GET.get("volunteering_id"))
    print("respuesta voluntariados")
    print(volunteering)

    volunteering = Volunteering.objects.get(id = request.GET.get("volunteering_id"))
    print("obtuvo el voluntariado")
    volunteeringVolunteers = Volunteer.objects.filter(volunteering = volunteering)
    print("obtuvo los voluntarios")
    volunteeringActivities = ActivitieDetailPage.objects.filter(volunteering = volunteering)
    print("obtuvo las actividades del voluntariado")
    last_restart = Restart.objects.all().order_by('-date').first()
    print("obtuvo el ultimo reinicio")

    if last_restart:
        last_restart = last_restart.date
    print("asigno la fecha del reinicio")

    #agrupar por volunteer
    attendances = Attendance.objects.filter(date__gte = last_restart, volunteer__in = volunteeringVolunteers, activity__in = volunteeringActivities)
    print("obtuvo asistencias")

    recordsVolunteersDict = {}

    for attendance in attendances:
        if attendance.volunteer in recordsVolunteersDict:
            recordsVolunteersDict[attendance.volunteer] += 1
        else:
            recordsVolunteersDict[attendance.volunteer] = 1
    
    for volunteer in volunteeringVolunteers:
            if not volunteer in recordsVolunteersDict:
                recordsVolunteersDict[volunteer] = 0
    print("llego al final")


    return render(request, "volunteerings/attendances.html",
                  {
                      "volunteers": volunteeringVolunteers,
                      "recordsVolunteersDict": recordsVolunteersDict,
                      "attendances": attendances,
                  })