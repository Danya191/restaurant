from django.urls import path
from .views import cart, add_to_cart, remove_from_cart
from . import views


app_name = 'shopping_cart'


urlpatterns = [
    path('add/<int:dish_id>/', views.add_to_cart, name='add_to_cart'),
    path('', cart, name='cart'),
    path('remove/<int:dish_id>/', remove_from_cart, name='remove_from_cart'),

]