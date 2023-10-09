from django.db import models
from allauth.account.forms import SignupForm
from django import forms

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
        return user
