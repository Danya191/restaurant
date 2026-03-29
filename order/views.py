from django.shortcuts import render

def order(request):
    total = request.session.get('total', 60)

    return render(request, 'order.html', {
        'total': total
    })