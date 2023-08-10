from django.urls import path
from .views import customer_upload_view
from .views import customers_list
from .views import customer_detail
from .views import customer_update_view



urlpatterns = [
    path("customers/upload/", customer_upload_view, name="customer_upload_view"),
    path("customers/list/", customers_list, name="customers_list_view"),
    path('customer/customers/edit/<int:id>/', customer_update_view, name='customer_update'),
    path("customers/<int:id>/", customer_detail, name="customer_detail_view"),
    

]