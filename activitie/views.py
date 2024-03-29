from django.shortcuts import render, get_object_or_404, redirect
from activitie.models import Volunteer, ActivitieDetailPage, User
from attendances.models import Attendance
from vehicles.models import Vehicle
from volunteerings.views import ViewVolunteering
from restart.models import Restart
from django.http import QueryDict
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
import datetime

def InscriptionView(request):
    user = get_object_or_404(User, id=request.user.id)
    activitie = get_object_or_404(ActivitieDetailPage, id=request.POST.get("actividad_id"))
    volunteer = get_object_or_404(Volunteer, user=user)
    if activitie.activity_start_date <= datetime.date.today() and activitie.activity_end_date > datetime.date.today():
        if activitie.volunteers.filter(id=volunteer.id).exists():
            activitie.volunteers.remove(volunteer)
            vehicle = volunteer.vehicles.filter(activitie = activitie)
            if vehicle:
                vehicle[0].activitie.remove(activitie)
                vehicle[0].save(force_update=True)
                if vehicle[0].domain == "Pasajero":
                    vehicle[0].delete()
        else:
            activitie.volunteers.add(volunteer)

    mutable_get = request.GET.copy()
    mutable_get['volunteering_id'] = request.POST.get("volunteering_id")
    request.GET = QueryDict(mutable_get.urlencode(), mutable=False)

    url_destino = f'/voluntariado/?volunteering_id={request.POST.get("volunteering_id")}'

    return redirect(url_destino)

def VisualizeEnrolledView(request):
    #verificar que quien acceda sea un coordinador
    activitie = get_object_or_404(ActivitieDetailPage, id=request.GET.get("actividad_id"))
    try:
        coordinator = Volunteer.objects.get(Q(user__id=request.user.id) & Q(user__is_superuser=True))
    except ObjectDoesNotExist:
        coordinator = Volunteer.objects.get(Q(user__id=request.user.id) & Q(coordinador=True) & Q(coordina__id=activitie.volunteering.id))

    volunteers = Volunteer.objects.filter(activities = activitie)
    vehicles = Vehicle.objects.filter(activitie = activitie)
    volunteersWithVehicle = Volunteer.objects.filter(vehicles__in=vehicles)

    return render(request,"activitie/activitie_enrolled.html",
                  {
                      "volunteers":volunteers,
                      "vehicles":vehicles,
                      "volunteersWithVehicle": volunteersWithVehicle,
                  },)

def TakeAttendance(request):
    #verificar que quien acceda sea un coordinador
    activitie = get_object_or_404(ActivitieDetailPage, id=request.GET.get("actividad_id"))
    try:
        coordinator = Volunteer.objects.get(Q(user__id=request.user.id) & Q(user__is_superuser=True))
    except ObjectDoesNotExist:
        coordinator = Volunteer.objects.get(Q(user__id=request.user.id) & Q(coordinador=True) & Q(coordina__id=activitie.volunteering.id))

    volunteers = Volunteer.objects.filter(activities = activitie)
    dateAttendance = Attendance.objects.filter(activity = activitie, date = datetime.date.today())
    volunteersPresent = set()
    for attendance in dateAttendance:
        volunteersPresent.add(attendance.volunteer)
    volunteersPresentList = list(volunteersPresent)

    return render(request, "activitie/activity_attendance.html",
                  {
                      "volunteers":volunteers,
                      "activity":activitie,
                      "volunteersPresentList": volunteersPresentList,

                  },)

def AddAttendance(request):
    #verificar que quien acceda sea un coordinador
    activity = get_object_or_404(ActivitieDetailPage, id=request.POST.get("actividad_id"))
    try:
        coordinator = Volunteer.objects.get(Q(user__id=request.user.id) & Q(user__is_superuser=True))
    except ObjectDoesNotExist:
        coordinator = Volunteer.objects.get(Q(user__id=request.user.id) & Q(coordinador=True) & Q(coordina__id=activity.volunteering.id))

    volunteersPresentId = set()
    for attendance in request.POST:
        if attendance != "actividad_id" and attendance != "csrfmiddlewaretoken":
            volunteersPresentId.add(int(attendance))
    
    volunteersPresentIdList = list(volunteersPresentId)
    volunteersPresent = Volunteer.objects.filter(id__in = volunteersPresentIdList)
    volunteers = Volunteer.objects.filter(activities = activity)
    records = Attendance.objects.filter(volunteer__in = volunteers, activity = activity, date = datetime.date.today())

    volunteersRecorded = set()

    for record in records:
        volunteersRecorded.add(record.volunteer)

    for record in records:
        if record.volunteer.id not in volunteersPresentIdList:
            record.delete()

    for volunteer in volunteersPresent:
        if volunteer not in volunteersRecorded:
            record = Attendance()
            record.activity = activity
            record.volunteer = volunteer
            record.date = datetime.date.today()
            record.activity_title = activity.custom_title
            record.save()

    mutable_get = request.GET.copy()
    mutable_get['actividad_id'] = request.POST.get("actividad_id")
    request.GET = QueryDict(mutable_get.urlencode(), mutable=False)
    
    url_destino = f'/voluntariado/?volunteering_id={activity.volunteering.id}'

    return redirect(url_destino)


def AttendanceRecord(request):
    #verificar que quien acceda sea un coordinador
    activity = get_object_or_404(ActivitieDetailPage, id=request.GET.get("actividad_id"))
    try:
        coordinator = Volunteer.objects.get(Q(user__id=request.user.id) & Q(user__is_superuser=True))
    except ObjectDoesNotExist:
        coordinator = Volunteer.objects.get(Q(user__id=request.user.id) & Q(coordinador=True) & Q(coordina__id=activity.volunteering.id))

    last_restart = Restart.objects.all().order_by('-date').first()
    records = None
    
    if last_restart:
        records = Attendance.objects.filter(date__gte = last_restart.date, activity = activity).order_by('-date', "volunteer__user__last_name")
    else:
        records = Attendance.objects.filter(activity = activity).order_by('-date', "volunteer__user__last_name")

    recordsDaysList = list()
    for record in records:
        if record.date not in recordsDaysList:
            recordsDaysList.append(record.date)
    

    return render(request, "activitie/attendance_record.html",
                  {
                      "records":records,
                      "recordsDaysList": recordsDaysList,
                      "activity": activity.title
                  },)

def VolunteerAttendanceRecord(request):
    #verificar que quien acceda sea un coordinador
    activity = get_object_or_404(ActivitieDetailPage, id=request.GET.get("actividad_id"))
    try:
        coordinator = Volunteer.objects.get(Q(user__id=request.user.id) & Q(user__is_superuser=True))
    except ObjectDoesNotExist:
        coordinator = Volunteer.objects.get(Q(user__id=request.user.id) & Q(coordinador=True) & Q(coordina__id=activity.volunteering.id))

    last_restart = Restart.objects.all().order_by('-date').first()
    records = None

    if last_restart:
        records = Attendance.objects.filter(date__gte = last_restart.date, activity = activity).order_by("volunteer__user__last_name", '-date')
    else:
        records = Attendance.objects.filter(activity = activity).order_by("volunteer__user__last_name", '-date')

    
    recordsVolunteersDict = {}

    for record in records:
        if record.volunteer in recordsVolunteersDict:
            recordsVolunteersDict[record.volunteer] += 1
        else:
            recordsVolunteersDict[record.volunteer] = 1
    

    return render(request, "activitie/volunteer_attendance_record.html",
                  {
                      "records":records,
                      "recordsVolunteersDict": recordsVolunteersDict,
                      "activity": activity.title
                  },)

def RestartInscription(request):
    #verificar que quien acceda sea un coordinador
    try:
        coordinator = Volunteer.objects.get(Q(user__id=request.user.id) & Q(user__is_superuser=True))
    except ObjectDoesNotExist:
        coordinator = Volunteer.objects.get(Q(user__id=request.user.id) & Q(coordinador=True) & Q(coordina__id=request.POST.get("volunteering_id")))

    activity = get_object_or_404(ActivitieDetailPage, id=request.POST.get("actividad_id"))
    vehicles = Vehicle.objects.filter(activitie = activity)

    activity.volunteers.clear()
    
    for vehicle in vehicles:
        vehicle.activitie.remove(activity)
        vehicle.save()

    mutable_get = request.GET.copy()
    mutable_get['volunteering_id'] = request.POST.get("volunteering_id")
    request.GET = QueryDict(mutable_get.urlencode(), mutable=False)

    url_destino = f'/voluntariado/?volunteering_id={request.POST.get("volunteering_id")}'

    return redirect(url_destino)
