from django.shortcuts import render, redirect
from .models import Order
from translations import LANGUAGES
from shopping_cart.models import CartItem

def order(request):

    lang = request.session.get("lang", "ru")
    total = 0

    cart_items = CartItem.objects.filter(user=request.user)

    for item in cart_items:
        total += item.dish.price * item.quantity

    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        Order.objects.create(
            name=name,
            surname=surname,
            address=address,
            phone=phone,
            total=total + 60
        )

        return redirect('/')

    return render(request, 'order.html', {
        'total': total,
        't': LANGUAGES[lang]
    })