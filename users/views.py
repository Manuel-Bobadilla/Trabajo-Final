from django.shortcuts import render
from users.models import User, Volunteer
from attendances.models import Attendance

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

# Create your views here.
