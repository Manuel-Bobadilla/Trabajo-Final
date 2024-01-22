from django.db import models
from allauth.account.forms import SignupForm, LoginForm
from django import forms
from users.models import Volunteer

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=25,
        label='',
        widget=forms.TextInput(attrs={"placeholder":("Nombre"), "class":("form-control")}),
    )
                                
    last_name = forms.CharField(max_length=25,
        label='',
        widget=forms.TextInput(attrs={"placeholder":("Apellido"), "class":("form-control")}),
    )

    address = forms.CharField(max_length=40,
        label='',
        widget=forms.TextInput(attrs={"placeholder":("Direccion"), "class":("form-control")}),
    )

    neighborhood = forms.CharField(max_length=40,
        label='',
        widget=forms.TextInput(attrs={"placeholder":("Barrio"), "class":("form-control")}),
    )

    phone = forms.CharField(max_length=40,
        label='',
        widget=forms.TextInput(attrs={"placeholder":("Telefono"), "class":("form-control")}),
    )

    birthdate = forms.DateField(
        label='Fecha de Nacimiento',
        widget=forms.DateInput(attrs={"type": "date", "class":("form-control")}),
    )

    dni = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={"placeholder": "Ingrese su DNI", "class":("form-control")}),
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
        label='',
        widget=forms.Select(attrs={"placeholder": "Selecciona una universidad", "class":("form-select")}),
    )

    university_file = forms.CharField(max_length=20,
        label='',
        widget=forms.TextInput(attrs={"placeholder":("Legajo universitario"), "class":("form-control")}),
    )

    career = forms.CharField(max_length=40,
        label='',
        widget=forms.TextInput(attrs={"placeholder":("Carrera universitaria"), "class":("form-control")}),
    )

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget = forms.HiddenInput()
        self.fields["username"].required = False
        self.fields["username"].initial = "default_username"
        self.fields["email"].widget.attrs['class'] = 'form-control'
        self.fields["email"].widget.attrs['placeholder'] = 'Email'
        self.fields["email"].label = ''
        self.fields["password1"].widget.attrs['class'] = 'form-control'
        self.fields["password1"].widget.attrs['placeholder'] = 'Contraseña'
        self.fields["password1"].label = ''
        self.fields["password2"].widget.attrs['class'] = 'form-control'
        self.fields["password2"].widget.attrs['placeholder'] = 'Repita su contraseña'
        self.fields["password2"].label = ''

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

class CustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields["login"].widget.attrs['class'] = 'form-control'
        self.fields["login"].label = ''
        self.fields["login"].widget.attrs['placeholder'] = 'Email'
        self.fields["password"].widget.attrs['class'] = 'form-control'
        self.fields["password"].label = ''
        self.fields["password"].widget.attrs['placeholder'] = 'Contraseña'
    