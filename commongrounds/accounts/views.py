from django.views.generic.edit import UpdateView, CreateView
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .forms import ProfileUpdateForm, ProfileRegisterForm


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = "profile_update.html"
    fields = ['display_name']

    def get_object(self, queryset=None):
        return self.request.user.profile
    
class ProfileRegisterView(CreateView):
    model = Profile
    template_name = "profile_register.html"
    fields = "__all__"

    def form_valid(self, form):
        form.instance.contributor = self.request.user.profile
        return super().form_valid(form)