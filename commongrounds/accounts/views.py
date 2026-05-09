from django.views.generic.edit import UpdateView, CreateView
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileUpdateForm, UserForm, ProfileForm
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

    
def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix='user')
        upf = ProfileForm(request.POST, prefix='userprofile')
        if uf.is_valid() * upf.is_valid():
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return redirect("/")
    else:
        uf = UserForm(prefix='user')
        upf = ProfileForm(prefix='userprofile')
        ctx = dict(userform=uf, userprofileform=upf)
    return render('templates/profile_register.html', ctx)