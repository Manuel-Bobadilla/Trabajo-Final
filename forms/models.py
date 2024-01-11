from django.db import models
from allauth.account.forms import SignupForm
from django import forms
from users.models import Volunteer

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=25,
        label='Nombre',
        widget=forms.TextInput(attrs={"placeholder":("Nombre"),}),
    )
                                
    last_name = forms.CharField(max_length=25,
        label='Apellido',
        widget=forms.TextInput(attrs={"placeholder":("Apellido"),}),
    )

    address = forms.CharField(max_length=40,
        label='Direccion',
        widget=forms.TextInput(attrs={"placeholder":("Direccion"),}),
    )

    neighborhood = forms.CharField(max_length=40,
        label='Barrio',
        widget=forms.TextInput(attrs={"placeholder":("Barrio"),}),
    )

    phone = forms.CharField(max_length=40,
        label='Teléfono',
        widget=forms.TextInput(attrs={"placeholder":("Telefono"),}),
    )

    birthdate = forms.DateField(
        label='Fecha de Nacimiento',
        widget=forms.DateInput(attrs={"type": "date"}),
    )

    dni = forms.CharField(
        label='DNI',
        widget=forms.TextInput(attrs={"placeholder": "Ingrese su DNI"}),
        #validators=[validators.RegexValidator(r'^\d{1,10}$', 'Ingrese un número válido.')],
    )

    UNIVERSITY_CHOICES = [
        ('UCC', 'Universidad Católica de Córdoba'),
        ('UTN', 'Universidad Tecnológica Nacional'),
        ('UNC', 'Universidad Nacional de Córdoba'),
        ('UBP', 'Universidad Blas Pascal'),
        ('SIGLO21', 'Universidad Siglo 21'),
        ('IUA', 'Instituto Universitario Aeronáutico'),
    ]

    university = forms.ChoiceField(
        choices=UNIVERSITY_CHOICES,
        label='Universidad',
        widget=forms.Select(attrs={"placeholder": "Selecciona una universidad"}),
    )

    university_file = forms.CharField(max_length=20,
        label='Legajo',
        widget=forms.TextInput(attrs={"placeholder":("Legajo universitario"),}),
    )

    career = forms.CharField(max_length=40,
        label='Carrera',
        widget=forms.TextInput(attrs={"placeholder":("Carrera universitaria"),}),
    )

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget = forms.HiddenInput()
        self.fields["username"].required = False
        self.fields["username"].initial = "default_username"

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = user.first_name + user.last_name
        user.save()
        datosExtra = {
            "address": self.cleaned_data['address'],
            "phone": self.cleaned_data['phone'],
            "neighborhood": self.cleaned_data['neighborhood'],
            "university": self.cleaned_data['university'],
            "university_file": self.cleaned_data['university_file'],
            "career": self.cleaned_data['career'],
            "birthdate": self.cleaned_data['birthdate'],
            "dni": self.cleaned_data['dni'],
        }
        self.createVolunteer(user, datosExtra, request)

        return user
    
    def createVolunteer(self, user, datosExtra, request):
        volunteer = Volunteer(user=user,
                              address=datosExtra['address'],
                              phone=datosExtra['phone'],
                              neighborhood=datosExtra['neighborhood'],
                              university=datosExtra['university'],
                              university_file=datosExtra['university_file'],
                              career=datosExtra['career'],
                              birthdate=datosExtra['birthdate'],
                              dni=datosExtra['dni'],
                              validated=False)
        volunteer.save()
    