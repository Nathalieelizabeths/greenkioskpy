from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Payment
from django.contrib import messages

def make_payment(request):
    if request.method == 'POST':
        payment_method = request.POST['payment_method']
        amount = request.POST['amount']
        status = 'P'  
        description = request.POST['description']

        payment = Payment(payment_method=payment_method, amount=amount, status=status, description=description)
        payment.save()

        messages.success(request, 'Payment request submitted successfully.')
        return redirect('payment_list')
    
    return render(request, 'make_payment.html')

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment/payment_list.html', {'payment': payments})
