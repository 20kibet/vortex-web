from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from orders.models import Order

@login_required
def dashboard(request):
    orders = Order.objects.filter(customer=request.user).order_by('-created_at')
    return render(request, 'dashboard/dashboard.html', {
        'orders': orders
    })