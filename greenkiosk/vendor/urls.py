from django.urls import path
from . import views

app_name = 'vendor'

urlpatterns = [
    path('vendors/list/', views.vendor_list, name='vendor_list'),
    path('vendors/<int:id>/', views.vendor_detail, name='vendor_detail'),
    path('vendors/create/', views.vendor_create, name='vendor_create'),
    path('vendors/<int:id>/edit/', views.vendor_edit, name='vendor_edit'),
    path('vendors/<int:id>/delete/', views.vendor_delete, name='vendor_delete'),
]
