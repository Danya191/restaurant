from django.urls import path
from .views import menu_page, DishDetailView

urlpatterns = [
    path('', menu_page, name='menu'),
    path('dish/<int:pk>/', DishDetailView.as_view(), name='dish-detail'),
]