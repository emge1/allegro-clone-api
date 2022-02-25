from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.user_roles.models.staff import Staff
from v1.user_roles.serializers.staff import StaffSerializer, StaffSerializerCreate
from v1.utils import constants
from v1.utils.permissions import is_administrator


# staff users
class StaffView(APIView):

    @staticmethod
    def get(request):
        """
        List staff users
        """

        staffs = Staff.objects.all()
        return Response(StaffSerializer(staffs, many=True).data)

    @staticmethod
    def post(request):
        """
        Create staff user
        """

        serializer = StaffSerializerCreate(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(StaffSerializer(serializer.instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# staff/{staff_id}
class StaffDetail(APIView):

    @staticmethod
    def delete(request, staff_id):
        """
        Delete moderator
        """

        staff = get_object_or_404(Staff, pk=staff_id)
        if not is_administrator(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_ADMINISTRATOR_REQUIRED
            }, status=status.HTTP_403_FORBIDDEN)
        staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
