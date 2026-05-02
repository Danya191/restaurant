from django.shortcuts import render
from .models import Dish, Category

def menu_page(request):
    category_id = request.GET.get('category')

    if category_id:
        dishes = Dish.objects.filter(category_id=category_id)
    else:
        dishes = Dish.objects.all()

    categories = Category.objects.all()

    return render(request, 'menu.html', {
        'dishes': dishes,
        'categories': categories
    })