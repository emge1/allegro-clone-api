from rest_framework import serializers
from v1.product_reviews.models.product_review import ProductReview


class ProductReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductReview
        fields = '__all__'


class ProductReviewSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ProductReview
        fields = '__all__'


class ProductReviewSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = ProductReview
        exclude = ('user',)

    def validate(self, data):
        """
        Validate authenticated user
        """

        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit product review from other users')
        return data
