from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Order
from customer.models import Customer

# Create your views here.

def create_order(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        order_number = request.POST.get('order_number')
        order_status = request.POST.get('order_status')

        try:
            customer = Customer.objects.get(id=customer_id)
            order = Order.objects.create(customer=customer, order_number=order_number, order_status=order_status)
            
            return redirect('order_list')
        except Customer.DoesNotExist:
            return render(request, 'error.html', {'message': 'Invalid customer ID'})

    customers = Customer.objects.all()
    return render(request, 'create_order.html', {'customers': customers})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})
