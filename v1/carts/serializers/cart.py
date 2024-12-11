from rest_framework import serializers
from v1.carts.models.cart import Cart
from v1.carts.serializers.cart_item import CartItemSerializer


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:

        model = Cart
        fields = ['user', 'items', 'updated_at', 'created_at']


