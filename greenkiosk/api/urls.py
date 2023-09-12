from django.urls import path
from .views import CustomerListView
from .views import CustomerDetailView
from .views import AddToCartView
urlpatterns = [
    path("customers/list/", CustomerListView.as_view(), name="customer_list_view"),
    path('customer/<int:id>/',CustomerDetailView.as_view(),name="customer_detail_view"),
    path("add_to_cart/",AddToCartView.as_view(),name ="add_to_cart"),
]
