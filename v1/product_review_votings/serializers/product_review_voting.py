from rest_framework import serializers
from v1.product_review_votings.models.product_review_voting import ProductReviewVoting


class ProductReviewVotingSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductReviewVoting
        fields = '__all__'


class ProductReviewVotingSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ProductReviewVoting
        fields = '__all__'


class ProductReviewVotingSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = ProductReviewVoting
        exclude = ('user',)

    def validate(self, data):
        """
        Validate authenticated user
        """

        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit product review voting from other users')
        return data
