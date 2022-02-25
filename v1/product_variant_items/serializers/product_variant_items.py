from rest_framework import serializers
from v1.product_variant_items.models.product_variant_items import ProductVariantItem


class ProductVariantItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductVariantItem
        fields = '__all__'


class ProductVariantItemSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ProductVariantItem
        fields = '__all__'


class ProductVariantItemSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = ProductVariantItem
        exclude = ('user',)

    def validate(self, data):
        """
        Validate authenticated user
        """

        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit product items from other users')
        return data
