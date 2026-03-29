from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import CartItem
from menu.models import Dish

# @login_required
# def add_to_cart(request, dish_id):
#     dish = Dish.objects.get(id=dish_id)

#     CartItem.objects.create(
#         user=request.user,
#         dish=dish
#     )

#     return redirect('shopping_cart:cart')  # можно 'cart' если хочешь сразу туда


# @login_required
# def cart(request):
#     items = CartItem.objects.filter(user=request.user)
#     return render(request, 'shopping_cart.html', {'items': items})


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

    request.session['total'] = total  # ← ВОТ КУДА ПИСАТЬ

    return render(request, 'shopping_cart/shopping_cart.html', {
        'dishes': dishes,
        'total': total
    })











# def cart(request):
#     cart = request.session.get('cart', [])

#     dishes = []

#     for dish_id in cart:
#         try:
#             dish = Dish.objects.get(id=dish_id)
#             dishes.append(dish)
#         except:
#             print("NOT FOUND:", dish_id)  # ← важно

#     print("DISHES:", dishes)  # ← главное



#     print("ALL DISHES:", Dish.objects.all())

#     return render(request, 'shopping_cart/shopping_cart.html', {'dishes': dishes})


def remove_from_cart(request, dish_id):
    cart = request.session.get('cart', [])

    if dish_id in cart:
        cart.remove(dish_id)

    request.session['cart'] = cart

    return redirect('shopping_cart:cart')



def cart_page(request):
    return render(request, 'shoping_cart.html')




# def cart(request):
#     cart = request.session.get('cart', [])

#     dishes = Dish.objects.filter(id__in=cart)
#     total = sum(dish.price for dish in dishes)

#     request.session['cart'] = list(dishes.values_list('id', flat=True))


#     return render(request, 'shopping_cart/shopping_cart.html', {
#         'dishes': dishes,
#         'total': total
#     })


