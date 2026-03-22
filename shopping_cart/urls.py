from django.urls import path
from .views import cart_page
from . import views


urlpatterns = [
    path('', cart_page, name='cart'),
    # path('add/<int:dish_id>/', views.add_to_cart, name='add_to_cart'),
]