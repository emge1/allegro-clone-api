from django.db import models
from v1.products.models.product import Product
from v1.user_roles.models.customer import Customer


class ProductReview(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    review_image = models.FileField()
    rating = models.CharField(default="5", max_length=255)
    review = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
