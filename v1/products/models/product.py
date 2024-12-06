from django.db import models
from v1.subcategories.models.subcategory import Subcategory
from v1.user_roles.models.merchant import Merchant


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    url_slug = models.CharField(max_length=255)
    subcategories_id = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    max_price = models.CharField(max_length=255)
    discount_price = models.CharField(max_length=255)
    thumbnail = models.ImageField(blank=True)
    description = models.TextField()
    long_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    in_stock_total = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
