from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import CartItem
from menu.models import Dish
from translations import LANGUAGES



from django.shortcuts import redirect, render
from menu.models import Dish

def add_to_cart(request, dish_id):
    print("CLICK WORKS")

    cart = request.session.get('cart', [])

    cart.append(dish_id)

    request.session['cart'] = cart  # ← ВАЖНО

    print("NEW CART:", cart)  # ← добавь

    return redirect('shopping_cart:cart')




def cart(request):

    lang = request.session.get("lang", "ru")

    cart = request.session.get('cart', [])

    dishes = []
    total = 0

    for dish_id in cart:
        try:
            dish = Dish.objects.get(id=dish_id)
            dishes.append(dish)
            total += dish.price
        except Dish.DoesNotExist:
            pass

    request.session['total'] = total

    return render(request, 'shopping_cart/shopping_cart.html', {
        'dishes': dishes,
        'total': total,
        't': LANGUAGES[lang]
    })



def remove_from_cart(request, dish_id):
    cart = request.session.get('cart', [])

    if dish_id in cart:
        cart.remove(dish_id)

    request.session['cart'] = cart

    return redirect('shopping_cart:cart')



def cart_page(request):
    return render(request, 'shoping_cart.html')





