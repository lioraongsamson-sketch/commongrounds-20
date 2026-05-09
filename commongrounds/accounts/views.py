from django.views.generic.edit import UpdateView, CreateView
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileUpdateForm, UserRegisterForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.template import RequestContext



class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = "profile_update.html"
    success_url = "/"

    def get_object(self, queryset=None):
        return self.request.user.profile


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = "profile_register.html"
    success_url = "/"