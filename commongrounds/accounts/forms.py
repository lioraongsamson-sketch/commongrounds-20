from django import forms
from .models import Profile
from django.contrib.auth.models import User


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name']


class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
