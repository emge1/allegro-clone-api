from django.db import models
from v1.product_variants.models.product_variant import ProductVariant
from v1.products.models.product import Product


class ProductVariantItem(models.Model):
    id = models.AutoField(primary_key=True)
    product_varient_id = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

