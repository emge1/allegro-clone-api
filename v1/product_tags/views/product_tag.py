from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.product_tags.models.product_tag import ProductTag
from v1.product_tags.serializers.product_tag import ProductTagSerializer, ProductTagSerializerCreate, \
    ProductTagSerializerUpdate
from v1.utils import constants
from v1.utils.permissions import is_merchant


# product_tags
class ProductTagView(APIView):

    @staticmethod
    def get(request):
        """
        List product tags
        """

        product_tag = ProductTag.objects.all()
        return Response(ProductTagSerializer(product_tag, many=True).data)

    @staticmethod
    def post(request):
        """
        Create product tag
        """

        serializer = ProductTagSerializerCreate(data=request.data, context={'request': request})
        if not is_merchant(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_MERCHANT_REQUIRED
            }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(ProductTagSerializer(serializer.instance).data)


# product_tags/{product_tag_id}
class ProductTagDetail(APIView):

    @staticmethod
    def get(request, product_tag_id):
        """
        View individual product tag
        """

        product_tag = get_object_or_404(ProductTag, pk=product_tag_id)
        return Response(ProductTagSerializer(product_tag).data)

    @staticmethod
    def patch(request, product_tag_id):
        """
        Update product tag
        """

        product_tag = get_object_or_404(ProductTag, pk=product_tag_id)
        serializer = ProductTagSerializerUpdate(product_tag, data=request.data, context={'request': request},
                                                partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(ProductTagSerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, product_tag_id):
        """
        Delete product tag
        """

        product_tag = get_object_or_404(ProductTag, pk=product_tag_id)
        if product_tag.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        product_tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
