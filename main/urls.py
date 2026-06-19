from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('language/<str:lang>/', views.set_language, name='set_language'),

]