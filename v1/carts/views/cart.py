from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from v1.carts.models.cart import Cart
from v1.carts.models.cart_item import CartItem
from v1.carts.serializers.cart import CartSerializer
from v1.user_roles.models.customer import Customer
from v1.products.models.product import Product
from decimal import Decimal, InvalidOperation


class CartView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Get User's Cart:
        """
        try:
            customer = Customer.objects.get(user=request.user)
            cart = Cart.objects.get(user=customer)
            serializer = CartSerializer(cart)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Cart.DoesNotExist:
            return Response({"detail": "The cart does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        """
        Post an Item to Cart:
        """
        print(request.data)
        customer = Customer.objects.get(user=request.user)
        try:
            cart = Cart.objects.get(user=customer)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=customer)

        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)
        price = request.data.get('price')

        if not price:
            return Response({"detail": "Price is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            price = Decimal(price)
        except InvalidOperation:
            return Response({"detail": "Invalid price format"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"detail": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity, "price": price},
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.price = price
            cart_item.save()

        return Response({"detail": "Product added to the cart"}, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        """
        Delete Item from Cart
        """
        product_id = request.data.get('product_id')
        customer = Customer.objects.get(user=request.user)

        try:
            cart = Cart.objects.get(user=customer)
        except Cart.DoesNotExist:
            return Response({"detail": "Cart does not exist"}, status=status.HTTP_404_NOT_FOUND)

        try:
            cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
            cart_item.delete()
            return Response({"detail": "Product removed from cart"}, status=status.HTTP_200_OK)
        except CartItem.DoesNotExist:
            return Response({"detail": "Cart does not exist in cart"}, status=status.HTTP_404_NOT_FOUND)
