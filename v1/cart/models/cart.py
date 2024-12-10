from django.db import models
from v1.user_roles.models.customer import Customer


class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
