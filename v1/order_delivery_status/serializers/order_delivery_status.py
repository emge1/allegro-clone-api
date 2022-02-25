from rest_framework import serializers
from v1.order_delivery_status.models.order_delivery_status import OrderDeliveryStatus


class OrderDeliveryStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDeliveryStatus
        fields = '__all__'


class OrderDeliveryStatusSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = OrderDeliveryStatus
        fields = '__all__'


class OrderDeliveryStatusSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = OrderDeliveryStatus
        fields = ('status', 'status_message',)
