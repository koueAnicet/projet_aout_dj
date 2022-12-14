from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model

class FormRegister(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = [

            "last_name", 
            "first_name", 
            "email", 
            "number",
            "username",
            "is_doctor",
            "is_patient",
            "service",
        ]
        

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label=" Nom d'utilisateur")
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')
    is_doctor = forms.BooleanField(required=False)
