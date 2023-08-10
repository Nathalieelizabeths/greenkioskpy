from django.contrib import admin
# Register your models here.
from .models import Order
class OrderAdmin(admin.ModelAdmin):
    list_display=("order_number","order_date","order_status")
admin.site.register(Order,OrderAdmin)