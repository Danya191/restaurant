from django.shortcuts import render
from django.views.generic import DetailView

from .models import Dish, Category
from translations import LANGUAGES
from django.shortcuts import redirect


def menu_page(request):

    lang = request.session.get("lang", "ru")

    category_id = request.GET.get('category')

    if category_id == 'all' or not category_id:
        dishes = Dish.objects.all()
    else:
        dishes = Dish.objects.filter(category_id=category_id)

    categories = Category.objects.all()

    return render(request, 'menu.html', {
        'dishes': dishes,
        'categories': categories,
        't': LANGUAGES[lang]
    })


class DishDetailView(DetailView):
    model = Dish
    template_name = 'menu/dish_detail.html'
    context_object_name = 'dish'





def set_language(request, lang):
    request.session["lang"] = lang
    return redirect(request.META.get("HTTP_REFERER", "/"))