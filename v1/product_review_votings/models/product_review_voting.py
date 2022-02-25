from django.db import models
from v1.product_reviews.models.product_review import ProductReview
from v1.user_roles.models.customer import Customer


class ProductReviewVoting(models.Model):
    id = models.AutoField(primary_key=True)
    product_review_id = models.ForeignKey(ProductReview, on_delete=models.CASCADE)
    user_id_voting = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
