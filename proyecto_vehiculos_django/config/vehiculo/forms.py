#Formulario Vehículos
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Vehiculo


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

        def save(self, commit=True):
            user = super(RegistroUsuarioForm, self).save(commit=False)
            user.email = self.cleaned_data['email']

            if commit:
                user.save()
            return user

class Form_ingreso_vehiculo(forms.ModelForm):

    class Meta:
        model = Vehiculo
        fields = '__all__'

    