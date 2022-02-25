from rest_framework import serializers
from v1.customer_orders.models.customer_order import CustomerOrder


class CustomerOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerOrder
        fields = '__all__'


class CustomerOrderSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CustomerOrder
        fields = '__all__'


class CustomerOrderSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = CustomerOrder
        exclude = ('user',)

    def validate(self, data):
        """
        Validate authenticated user
        """

        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit order from other users')
        return data
