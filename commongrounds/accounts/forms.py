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
        fields = ['username', 'email', 'password']

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