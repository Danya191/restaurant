from django.shortcuts import render
from .models import Dish

def menu_page(request):
    return render(request, 'menu.html')


def menu_page(request):
    dishes = Dish.objects.all()
    return render(request, 'menu.html', {'dishes': dishes})