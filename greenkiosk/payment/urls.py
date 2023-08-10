from django.urls import path
from . import views

urlpatterns = [
    path('make_payment/', views.make_payment, name='make_payment'),
    path('payment_list/', views.payment_list, name='payment_list'),
]
