from rest_framework import serializers
from v1.carts.models.cart_item import CartItem
from v1.products.serializers.product import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'price']



