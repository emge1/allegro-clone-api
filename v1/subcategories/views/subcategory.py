from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.subcategories.models.subcategory import Subcategory
from v1.subcategories.serializers.subcategory import SubcategorySerializer, SubcategorySerializerCreate, \
    SubcategorySerializerUpdate
from v1.utils import constants
from v1.utils.permissions import is_administrator


# subcategories
class SubcategoryView(APIView):

    @staticmethod
    def get(request):
        """
        List subcategories
        """

        subcategories = Subcategory.objects.all()
        return Response(SubcategorySerializer(subcategories, many=True).data)

    @staticmethod
    def post(request):
        """
        Create subcategory
        """

        serializer = SubcategorySerializerCreate(data=request.data, context={'request': request})
        if not is_administrator(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_ADMINISTRATOR_REQUIRED
            }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(SubcategorySerializer(serializer.instance).data)


# subcategories/{subcategory_id}
class SubcategoryDetail(APIView):

    @staticmethod
    def get(request, subcategory_id):
        """
        View individual subcategory
        """

        subcategories = get_object_or_404(Subcategory, pk=subcategory_id)
        return Response(SubcategorySerializer(subcategories).data)

    @staticmethod
    def patch(request, subcategory_id):
        """
        Update subcategory
        """

        subcategory = get_object_or_404(Subcategory, pk=subcategory_id)
        serializer = SubcategorySerializerUpdate(subcategory, data=request.data, context={'request': request}, partial=True)
        if not is_administrator(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_ADMINISTRATOR_REQUIRED
            }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(SubcategorySerializer(serializer.instance).data)

    @staticmethod
    def delete(request, subcategory_id):
        """
        Delete subcategory
        """

        subcategory = get_object_or_404(Subcategory, pk=subcategory_id)
        if not is_administrator(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_ADMINISTRATOR_REQUIRED
            }, status=status.HTTP_401_UNAUTHORIZED)
        subcategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
