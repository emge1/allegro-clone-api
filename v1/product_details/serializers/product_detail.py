from rest_framework import serializers
from v1.product_details.models.product_detail import ProductDetail


class ProductDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductDetail
        fields = '__all__'


class ProductDetailSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ProductDetail
        fields = '__all__'


class ProductDetailSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = ProductDetail
        exclude = ('user',)

    def validate(self, data):
        """
        Validate authenticated user
        """

        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit product detail from other users')
        return data
