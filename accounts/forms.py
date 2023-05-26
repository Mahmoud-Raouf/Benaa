from django import forms
from .models import * 
from django.contrib.auth.models import User

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ("name","description" , "phone1" , "phone2", "description" , "address")



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username" , "password")


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username" , "email")



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("name" , "phone", "country", "address", "image")

