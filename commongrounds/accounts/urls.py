from django.urls import path
from .views import ProfileUpdateView, register

urlpatterns = [
    path('register/', register, name="profile_register"),
    path('<str:username>/', ProfileUpdateView.as_view(), name="profile_update"),
]
app_name = 'accounts'
