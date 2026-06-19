from django.urls import path
from .views import menu_page, DishDetailView
from . import views

urlpatterns = [
    path('', menu_page, name='menu'),
    path('dish/<int:pk>/', DishDetailView.as_view(), name='dish-detail'),
    path('language/<str:lang>/', views.set_language, name='set_language'),
]