from django.urls import path
from .views import register, profile, edit_profile

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]