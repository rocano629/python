from django import forms
from django.contrib.auth.models import User
from basic_app.models import USerProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta():
        model = User
        fields = ('username','email','password')

class USerProfileInfoForm(forms.ModelForm):
    class Meta():
        model = USerProfileInfo
        fields = ('portfolio_site','profile_pic')