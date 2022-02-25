from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.categories.models.category import Category
from v1.categories.serializers.category import CategorySerializer, CategorySerializerCreate, CategorySerializerUpdate
from v1.utils import constants
from v1.utils.permissions import is_administrator


# categories
class CategoryView(APIView):

    @staticmethod
    def get(request):
        """
        List categories
        """

        categories = Category.objects.all()
        return Response(CategorySerializer(categories, many=True).data)

    @staticmethod
    def post(request):
        """
        Create category
        """

        serializer = CategorySerializerCreate(data=request.data, context={'request': request})
        if not is_administrator(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_ADMINISTRATOR_REQUIRED
            }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(CategorySerializer(serializer.instance).data)


# categories/{category_id}
class CategoryDetail(APIView):

    @staticmethod
    def get(request, category_id):
        """
        View individual category
        """

        category = get_object_or_404(Category, pk=category_id)
        return Response(CategorySerializer(category).data)

    @staticmethod
    def patch(request, category_id):
        """
        Update category
        """

        category = get_object_or_404(Category, pk=category_id)
        serializer = CategorySerializerUpdate(category, data=request.data, context={'request': request}, partial=True)
        if not is_administrator(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_ADMINISTRATOR_REQUIRED
            }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(CategorySerializer(serializer.instance).data)

    @staticmethod
    def delete(request, category_id):
        """
        Delete category
        """

        category = get_object_or_404(Category, pk=category_id)
        if not is_administrator(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_ADMINISTRATOR_REQUIRED
            }, status=status.HTTP_401_UNAUTHORIZED)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
