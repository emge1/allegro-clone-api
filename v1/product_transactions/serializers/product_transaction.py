from rest_framework import serializers
from v1.product_transactions.models.product_transaction import ProductTransaction


class ProductTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductTransaction
        fields = '__all__'


class ProductTransactionSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ProductTransaction
        fields = '__all__'
