from django.contrib import admin
from .models import Order

# Register your models here.
class Order_Admin(admin.ModelAdmin):
    list_display=('name','customer_id','quantity','price')
admin.site.register(Order, Order_Admin)
