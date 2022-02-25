from rest_framework import serializers
from v1.subcategories.models.subcategory import Subcategory


class SubcategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = '__all__'


class SubcategorySerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Subcategory
        fields = '__all__'


class SubcategorySerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = ('title', 'description', 'is_active',)
