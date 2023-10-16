from django.shortcuts import render, get_object_or_404, redirect
from activitie.models import Volunteer, ActivitieDetailPage, User
from attendances.models import Attendance
from vehicles.models import Vehicle
from volunteerings.views import ViewVolunteering
import datetime

def InscriptionView(request, pk):
    user = get_object_or_404(User, id=request.user.id)
    activitie = get_object_or_404(ActivitieDetailPage, id=request.POST.get("actividad_id"))
    volunteer = get_object_or_404(Volunteer, user=user)
    if activitie.activity_start_date <= datetime.date.today() and activitie.activity_end_date > datetime.date.today():
        if activitie.volunteers.filter(id=volunteer.id).exists():
            activitie.volunteers.remove(volunteer)
            vehicle = volunteer.vehicles.filter(activitie = activitie)
            if vehicle:
                vehicle[0].activitie = None
                vehicle[0].save(force_update=True)
        else:
            activitie.volunteers.add(volunteer)

    return ViewVolunteering(request) #cambiar para que determine la url de retorno de manera dinamica

def VisualizeEnrolledView(request):
    activitie = get_object_or_404(ActivitieDetailPage, id=request.POST.get("actividad_id"))
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
    activitie = get_object_or_404(ActivitieDetailPage, id=request.POST.get("actividad_id"))
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
    volunteersPresentId = set()
    for attendance in request.POST:
        if attendance != "actividad_id" and attendance != "csrfmiddlewaretoken":
            volunteersPresentId.add(attendance)
    volunteersPresentIdList = list(volunteersPresentId)
    volunteersPresent = Volunteer.objects.filter(id__in = volunteersPresentIdList)
    activity = get_object_or_404(ActivitieDetailPage, id=request.POST.get("actividad_id"))
    volunteers = Volunteer.objects.filter(activities = activity)
    records = Attendance.objects.filter(volunteer__in = volunteers, activity = activity, date = datetime.date.today())
    for record in records:
        if record.volunteer.id not in volunteersPresentIdList:
            record.delete()

    for volunteer in volunteersPresent:
        record = Attendance()
        record.activity = activity
        record.volunteer = volunteer
        record.date = datetime.date.today()
        record.save()
    
    return TakeAttendance(request)


def AttendanceRecord(request):
    activity = get_object_or_404(ActivitieDetailPage, id=request.POST.get("actividad_id"))
    records = Attendance.objects.filter(activity = activity)
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
    activity = get_object_or_404(ActivitieDetailPage, id=request.POST.get("actividad_id"))
    records = Attendance.objects.filter(activity = activity)
    recordsVolunteersList = list()
    for record in records:
        if record.volunteer not in recordsVolunteersList:
            recordsVolunteersList.append(record.volunteer)
    

    return render(request, "activitie/volunteer_attendance_record.html",
                  {
                      "records":records,
                      "recordsVolunteersList": recordsVolunteersList,
                      "activity": activity.title
                  },)
