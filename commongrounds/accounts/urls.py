from django.urls import path
from .views import ProfileUpdateView, RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="profile_register"),
    path('<str:username>/', ProfileUpdateView.as_view(), name="profile_update"),
]
app_name = 'accounts'
