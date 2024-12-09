from rest_framework import serializers
from v1.cart.models.cart import Cart
from v1.cart.serializers.cart_item import CartItemSerializer


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    class Meta:
        model = Cart
        fields = ['id', 'product', 'quantity', 'price']


