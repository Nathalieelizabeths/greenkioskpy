from django.urls import path
from .views import make_payment, payment_list


# urls.py

urlpatterns = [
    path('payment/make/', make_payment, name='make_payment'),
    path('payment/list/', payment_list, name='payment_list'),
]
