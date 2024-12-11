from rest_framework import serializers
from v1.carts.models.cart_item import CartItem


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'price']



