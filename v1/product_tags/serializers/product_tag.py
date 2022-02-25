from rest_framework import serializers
from v1.product_tags.models.product_tag import ProductTag


class ProductTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductTag
        fields = '__all__'


class ProductTagSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ProductTag
        fields = '__all__'


class ProductTagSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = ProductTag
        exclude = ('user',)

    def validate(self, data):
        """
        Validate authenticated user
        """

        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit product tag from other users')
        return data
