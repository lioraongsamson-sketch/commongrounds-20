from django.views.generic.edit import UpdateView, CreateView
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileUpdateForm, UserRegisterForm



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