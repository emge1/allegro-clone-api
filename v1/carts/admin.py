from django.contrib import admin
from .models.cart import Cart
from .models.cart_item import CartItem


admin.site.register(Cart)
admin.site.register(CartItem)
