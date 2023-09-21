from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from captcha.fields import CaptchaField

class CustomUserCreation(UserCreationForm):



    class Meta:
        model = CustomUser
        fields = ['username', 'email','password1', 'password2','id_code','mobile','image']

    
class CaptchaForm(forms.Form):
    captcha = CaptchaField()