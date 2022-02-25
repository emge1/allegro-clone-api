from rest_framework import serializers
from v1.accounts.serializers.user import UserSerializer
from v1.user_roles.models.merchant import Merchant


class MerchantSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Merchant
        fields = '__all__'