from django.db import models
from product.models import Product
from order.models import Order

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='im_employee/%Y/%m/%d', null=True, blank=True)

class Seller(Employee):
    position = 'seller'

class ShopAssistant(models.Model):
    position = 'shop assistant'

class Bookkeeper(models.Model):
    position = 'book keeper'