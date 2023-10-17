from django.shortcuts import render
from users.models import User, Volunteer
from attendances.models import Attendance

def VolunteerAttendanceView(request):
    user = User.objects.get(id = request.user.id)
    volunteer = Volunteer.objects.get(user = user)
    records = Attendance.objects.filter(volunteer = volunteer).order_by('-date')
    recordsActivityList = list()

    for record in records:
        if record.activity not in recordsActivityList:
            recordsActivityList.append(record.activity)

    return render(request, "users/attendance.html",
                  {
                      "records":records,
                      "recordsActivityList":recordsActivityList,
                  },)

# Create your views here.
