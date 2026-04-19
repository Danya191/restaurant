from django.shortcuts import render, redirect
from .models import Order

def order(request):
    total = request.session.get('total', 0)


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
        'total': total
    })