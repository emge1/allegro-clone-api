from rest_framework import serializers
from v1.product_abouts.models.product_about import ProductAbout


class ProductAboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductAbout
        fields = '__all__'


class ProductAboutSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ProductAbout
        fields = '__all__'


class ProductAboutSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = ProductAbout
        exclude = ('user',)

    def validate(self, data):
        """
        Validate authenticated user
        """

        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit product about from other users')
        return data
