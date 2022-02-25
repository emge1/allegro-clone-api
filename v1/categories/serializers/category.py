from rest_framework import serializers
from v1.categories.models.category import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CategorySerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = '__all__'


class CategorySerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('title', 'description', 'is_active',)
