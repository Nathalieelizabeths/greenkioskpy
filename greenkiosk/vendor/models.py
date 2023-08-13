from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(default='default_vendor_image.png')
    address = models.CharField(max_length=200, null=True, blank=True) 

    