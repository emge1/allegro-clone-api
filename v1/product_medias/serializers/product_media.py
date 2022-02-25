from rest_framework import serializers
from v1.product_medias.models.product_media import ProductMedia


class ProductMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductMedia
        fields = '__all__'


class ProductMediaSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ProductMedia
        fields = '__all__'


class ProductMediaSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = ProductMedia
        exclude = ('user',)

    def validate(self, data):
        """
        Validate authenticated user
        """

        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit product medias from other users')
        return data
