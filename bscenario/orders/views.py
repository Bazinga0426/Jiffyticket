from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Order
from django.contrib.auth.decorators import login_required


@login_required
def order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'orders/detail.html', {'order': order})


@login_required
def list(request):
    user = request.user
    orders = user.order_set.all()
    return render(request, 'orders/list.html', {'orders': orders})


@login_required
def cancel(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.status = order.CANCELLED
    order.save()
    return render(request, 'orders/cancelled_done.html', {'order': order})


@login_required
def complete(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.status = order.COMPLETED
    order.save()
    return render(request, 'orders/completed_done.html', {'order': order})
