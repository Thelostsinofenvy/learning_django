from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo


class UserForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'Password')


class UserProfileInfoForms(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
