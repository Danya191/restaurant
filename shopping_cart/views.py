from django.shortcuts import render
# from django.shortcuts import redirect
# from django.contrib.auth.decorators import login_required
# from .models import CartItem
# from menu.models import Dish


# @login_required
# def add_to_cart(request, dish_id):
#     dish = Dish.objects.get(id=dish_id)

#     CartItem.objects.create(
#         user=request.user,
#         dish=dish
#     )

#     return redirect('cart') 



def cart_page(request):
    return render(request, 'shoping_cart.html')