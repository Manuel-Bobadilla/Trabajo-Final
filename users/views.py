from django.shortcuts import render
from users.models import User, Volunteer
from attendances.models import Attendance
from django.db.models import Q

def VolunteerAttendanceView(request):
    user = User.objects.get(id = request.user.id)
    volunteer = Volunteer.objects.get(user = user)
    records = Attendance.objects.filter(volunteer = volunteer).order_by('-date')
    recordsActivityList = {}

    for record in records:
        activity = None
        if record.activity:
            activity = record.activity
        else:
            activity = record.activity_title
        if activity in recordsActivityList:
            recordsActivityList[activity] += 1
        else:
            recordsActivityList[activity] = 1

    return render(request, "users/attendance.html",
                  {
                      "records":records,
                      "recordsActivityList":recordsActivityList,
                  },)

def ViewVolunteers(request):
    volunteers = None
    records = None
    recordsVolunteersDict = None

    if(request.GET.get("search")):
        wordsSearch = request.GET.get("search").split()
        query = Q()

        for word in wordsSearch:
            query &= Q(user__first_name__icontains=word) | Q(user__last_name__icontains=word) | Q(dni__icontains=word)
            
        volunteers = Volunteer.objects.filter(query)
        records = Attendance.objects.filter(volunteer__in = volunteers).order_by("volunteer__user__last_name", '-date')
        recordsVolunteersDict = {}

        for record in records:
            if record.volunteer in recordsVolunteersDict:
                recordsVolunteersDict[record.volunteer] += 1
            else:
                recordsVolunteersDict[record.volunteer] = 1

        for volunteer in volunteers:
            if not volunteer in recordsVolunteersDict:
                recordsVolunteersDict[volunteer] = 0

    return render(request, "users/volunteers.html",
                  {
                      "volunteers": volunteers,
                      "recordsVolunteersDict": recordsVolunteersDict,
                      "records": records,
                  })
