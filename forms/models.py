from django.db import models
from allauth.account.forms import SignupForm
from django import forms
from users.models import Volunteer

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=25,
                                  label='First Name',
                                  widget=forms.TextInput(attrs={"placeholder":("Nombre"),}),
                                  )
    last_name = forms.CharField(max_length=25,
                                 label='Last Name',
                                 widget=forms.TextInput(attrs={"placeholder":("Apellido"),}),
                                 )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        self.createVolunteer(user, request)

        return user
    
    def createVolunteer(self, user, request):
        volunteer = Volunteer(user=user,
                              address="calle1",
                              phone="3211231231",
                              neighborhood="barrio",
                              university="UCC",
                              university_file="0000000",
                              career="carrera",
                              birthdate=None,
                              dni="11111111",
                              validated=False)
        volunteer.save()
    