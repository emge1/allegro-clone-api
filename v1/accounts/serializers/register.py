from rest_framework import serializers
from v1.accounts.models.user import User


class RegisterSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'type_choice']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
