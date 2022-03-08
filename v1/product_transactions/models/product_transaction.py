from django.db import models
from v1.products.models.product import Product


class ProductTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_count = models.IntegerField(default=1)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
