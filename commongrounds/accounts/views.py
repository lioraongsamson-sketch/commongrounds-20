from django.views.generic.edit import UpdateView, CreateView
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileUpdateForm, ProfileRegisterForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy



class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = "profile_update.html"
    success_url = "/"

    def get_object(self, queryset=None):
        return self.request.user.profile

    
class ProfileRegisterView(CreateView):
    model = User
    form_class = ProfileRegisterForm
    template_name = "profile_register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.instance.user = self.request.user.profile
        return super().form_valid(form)
