from django.urls import path
from .views import CustomerListView
from .views import CustomerDetailView
urlpatterns = [
    path("customers/list/", CustomerListView.as_view(), name="customer_list_view"),
    path('customer/<int:id>/',CustomerDetailView.as_view(),name="customer_detail_view"),
]
