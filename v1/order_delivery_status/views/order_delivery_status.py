from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.order_delivery_status.models.order_delivery_status import OrderDeliveryStatus
from v1.order_delivery_status.serializers.order_delivery_status import OrderDeliveryStatusSerializer, \
    OrderDeliveryStatusSerializerCreate, OrderDeliveryStatusSerializerUpdate
from v1.customer_orders.models.customer_order import CustomerOrder
from v1.customer_orders.serializers.customer_order import CustomerOrderSerializer
from v1.products.models.product import Product
from v1.products.serializers.product import ProductSerializer
from v1.utils import constants
from v1.utils.permissions import is_merchant


# order_delivery_status
class OrderDeliveryStatusView(APIView):

    @staticmethod
    def post(request):
        """
        Create order delivery status
        """

        serializer = OrderDeliveryStatusSerializerCreate(data=request.data, context={'request': request})

        if not is_merchant(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_MERCHANT_REQUIRED
            }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(OrderDeliveryStatusSerializer(serializer.instance).data)


# order_delivery_status/{order_delivery_status_id}
class OrderDeliveryStatusDetail(APIView):

    @staticmethod
    def get(request, order_delivery_status_id):
        """
        View individual order delivery status
        """

        order_delivery_status = get_object_or_404(OrderDeliveryStatus, pk=order_delivery_status_id)

        serializer = OrderDeliveryStatusSerializer(order_delivery_status, data=request.data,
                                                   context={'request': request})
        order_id = serializer.data['order_id']
        order = get_object_or_404(CustomerOrder, pk=order_id)

        order_serializer = CustomerOrderSerializer(order_id, data=request.data, context={'request': request})
        product_id = order_serializer.data['product_id']
        product = get_object_or_404(Product, pk=product_id)

        if order.user != request.user or product.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(OrderDeliveryStatusSerializer(serializer.instance).data)

    @staticmethod
    def patch(request, order_delivery_status_id):
        """
        Update order delivery status
        """
        order_delivery_status = get_object_or_404(OrderDeliveryStatus, pk=order_delivery_status_id)
        serializer = OrderDeliveryStatusSerializerUpdate(order_delivery_status, data=request.data,
                                                         context={'request': request}, partial=True)

        order_id = serializer.data['product_id']

        order_serializer = CustomerOrderSerializer(order_id, data=request.data, context={'request': request})
        product_id = order_serializer.data['product_id']
        product = get_object_or_404(Product, pk=product_id)

        if product.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer.save()
        return Response(OrderDeliveryStatusSerializer(serializer.instance).data)

    @staticmethod
    def delete(request, order_delivery_status_id):
        """
        Delete order delivery status
        """

        order_delivery_status = get_object_or_404(OrderDeliveryStatus, pk=order_delivery_status_id)
        serializer = OrderDeliveryStatusSerializer(order_delivery_status, data=request.data,
                                                   context={'request': request})
        order_id = serializer.data['order_id']
        order = get_object_or_404(CustomerOrder, pk=order_id)

        if order.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        order_delivery_status.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
