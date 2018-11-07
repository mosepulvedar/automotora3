from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError

class CustomUserForm(UserCreationForm):
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")
    email = forms.EmailField(required=True)
    
    def clean_email(self):
        
        email = self.cleaned_data['email']
        existe = User.objects.filter(email=email)

        if existe:
            raise ValidationError("El email ya existe")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

