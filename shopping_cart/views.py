from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import CartItem
from menu.models import Dish
from translations import LANGUAGES



from django.shortcuts import redirect, render
from menu.models import Dish

from .models import CartItem

def add_to_cart(request, dish_id):

    item, created = CartItem.objects.get_or_create(
        user=request.user,
        dish_id=dish_id
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect('shopping_cart:cart')



def cart(request):

    lang = request.session.get("lang", "ru")

    cart_items = CartItem.objects.filter(
        user=request.user
    )

    total = 0

    for item in cart_items:
        total += item.dish.price * item.quantity

    return render(
        request,
        'shopping_cart/shopping_cart.html',
        {
            'cart_items': cart_items,
            'total': total,
            't': LANGUAGES[lang]
        }
    )



def remove_from_cart(request, item_id):

    CartItem.objects.filter(
        id=item_id,
        user=request.user
    ).delete()

    return redirect('shopping_cart:cart')



def cart_page(request):
    return render(request, 'shoping_cart.html')


def increase_quantity(request, item_id):

    item = CartItem.objects.get(
        id=item_id,
        user=request.user
    )

    item.quantity += 1
    item.save()

    return redirect('shopping_cart:cart')


def decrease_quantity(request, item_id):

    item = CartItem.objects.get(
        id=item_id,
        user=request.user
    )

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('shopping_cart:cart')





