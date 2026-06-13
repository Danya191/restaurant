from django.shortcuts import render
from .models import Dish, Category
from django.views.generic import DetailView

def menu_page(request):
    category_id = request.GET.get('category')

    if category_id == 'all' or not category_id:
        dishes = Dish.objects.all()
    else:
        dishes = Dish.objects.filter(category_id=category_id)

    categories = Category.objects.all()

    return render(request, 'menu.html', {
        'dishes': dishes,
        'categories': categories
    })



class DishDetailView(DetailView):
    model = Dish
    template_name = 'menu/dish_detail.html'
    context_object_name = 'dish'
