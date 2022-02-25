from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.customer_orders.models.customer_order import CustomerOrder
from v1.customer_orders.serializers.customer_order import CustomerOrderSerializer, CustomerOrderSerializerCreate, \
    CustomerOrderSerializerUpdate
from v1.products.models.product import Product
from v1.utils import constants
from v1.utils.permissions import is_customer


# customer_order
class CustomerOrderView(APIView):

    @staticmethod
    def post(request):
        """
        Create customer order
        """

        serializer = CustomerOrderSerializerCreate(data=request.data, context={'request': request})
        if not is_customer(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_MERCHANT_REQUIRED
            }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(CustomerOrderSerializer(serializer.instance).data)


# customer_orders/{customer_order_id}
class CustomerOrderDetail(APIView):

    @staticmethod
    def get(request, customer_order_id):
        """
        View individual customer order
        """

        customer_order = get_object_or_404(CustomerOrder, pk=customer_order_id)
        serializer = CustomerOrderSerializer(customer_order).data

        product_id = serializer.data['product_id']
        product = get_object_or_404(Product, pk=product_id)

        if customer_order.user != request.user or product.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(CustomerOrderSerializer(customer_order).data)

    @staticmethod
    def patch(request, customer_order_id):
        """
        Update customer order
        """

        customer_order = get_object_or_404(CustomerOrder, pk=customer_order_id)
        serializer = CustomerOrderSerializerUpdate(customer_order, data=request.data, context={'request': request},
                                                   partial=True)
        product_id = serializer.data['product_id']
        product = get_object_or_404(Product, pk=product_id)

        if customer_order.user != request.user or product.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer.save()
        return Response(CustomerOrderSerializer(customer_order).data)


    @staticmethod
    def delete(request, customer_order_id):
        """
        Delete customer order
        """

        customer_order = get_object_or_404(CustomerOrder, pk=customer_order_id)
        if customer_order.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        customer_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
