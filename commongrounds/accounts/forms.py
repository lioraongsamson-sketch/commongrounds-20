from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name']


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        role = forms.ChoiceField(
            choices=[
                ("None", "None"),
                ("Market Seller", "Market Seller"),
                ("Event Organizer", "Event Organizer"),
                ("Book Contributor", "Book Contributor"),
                ("Project Creator", "Project Creator"),
                ("Commission Maker", "Commission Maker"),
            ],
        )
        fields = ['role']