from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name']


class UserRegisterForm(UserCreationForm):
    display_name = forms.CharField(max_length=63)
    email = forms.EmailField()
    role = forms.ChoiceField(choices=Profile._meta.get_field("role").choices)

    class Meta:
        model = User
        fields = ["username","display_name","email","role","password1","password2",]

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data["email"]

        if commit:
            user.save()

            Profile.objects.create(
                user=user,
                display_name=self.cleaned_data["display_name"],
                email=self.cleaned_data["email"],
                role=self.cleaned_data["role"],
            )

        return user