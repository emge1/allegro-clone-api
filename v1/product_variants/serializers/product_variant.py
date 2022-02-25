from rest_framework import serializers
from v1.product_variants.models.product_variant import ProductVariant


class ProductVariantSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductVariant
        fields = '__all__'


class ProductVariantSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ProductVariant
        fields = '__all__'


class ProductVariantSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = ProductVariant
        exclude = ('user',)

    def validate(self, data):
        """
        Validate authenticated user
        """

        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit product tags from other users')
        return data
