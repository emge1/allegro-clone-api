from django.db import models
from v1.products.models.product import Product
from v1.utils.constants import MEDIA_TYPE_CHOICES


class ProductMedia(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=31,
        choices=MEDIA_TYPE_CHOICES,
        default=1
    )
    content = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
