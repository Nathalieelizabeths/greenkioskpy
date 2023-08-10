from django.db import models
from customer.models import Customer
# Create your models here.
class Order(models.Model):
    customer=models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    order_number = models.CharField(max_length=32, unique=True)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=16, choices=[
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'CanceLled'),
    ])