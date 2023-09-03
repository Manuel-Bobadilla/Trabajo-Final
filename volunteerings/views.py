from django.shortcuts import render
from volunteerings.models import Volunteering

def Volunteerings(request):
    volunteerings = Volunteering.objects.all()

    return render(request, "volunteerings/volunteerings.html",{"volunteerings":volunteerings,})
