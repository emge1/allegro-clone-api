from rest_framework import serializers
from v1.accounts.serializers.user import UserSerializer
from v1.user_roles.models.staff import Staff
from v1.utils import constants
from v1.utils.permissions import is_administrator, is_staff


class StaffSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Staff
        fields = '__all__'


class StaffSerializerCreate(serializers.ModelSerializer):
    sponsor = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Staff
        fields = '__all__'

    def validate(self, data):
        """
        Administrator permissions needed
        """

        if not is_administrator(self.context['request'].user):
            raise serializers.ValidationError(constants.PERMISSION_ADMINISTRATOR_REQUIRED)
        return data

    def validate_user(self, user):
        """
        Ensure user is not already moderator or higher
        """

        if is_staff(user):
            raise serializers.ValidationError('User already has staff permissions')
        return user
