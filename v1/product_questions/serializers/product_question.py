from rest_framework import serializers
from v1.product_questions.models.product_question import ProductQuestion


class ProductQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductQuestion
        fields = '__all__'


class ProductQuestionCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ProductQuestion
        exclude = ('answer',)


class ProductQuestionAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductQuestion
        fields = ('answer',)
