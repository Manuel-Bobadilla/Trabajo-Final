from django.shortcuts import render
from users.models import User, Volunteer
from attendances.models import Attendance
from activitie.models import ActivitieDetailPage

def VolunteerAttendanceView(request):
    user = User.objects.get(id = request.user.id)
    volunteer = Volunteer.objects.get(user = user)
    records = Attendance.objects.filter(volunteer = volunteer)

    return render(request, "users/attendance.html",
                  {
                      "records":records,
                  },)

# Create your views here.
