from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.product_medias.models.product_media import ProductMedia
from v1.product_medias.serializers.product_media import ProductMediaSerializer, ProductMediaSerializerCreate, \
    ProductMediaSerializerUpdate
from v1.utils import constants
from v1.utils.permissions import is_merchant


# product_medias
class ProductMediaView(APIView):

    @staticmethod
    def get(request):
        """
        List product medias
        """

        product_medias = ProductMedia.objects.all()
        return Response(ProductMediaSerializer(product_medias, many=True).data)

    @staticmethod
    def post(request):
        """
        Create product media
        """

        serializer = ProductMediaSerializerCreate(data=request.data, context={'request': request})
        if not is_merchant(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_MERCHANT_REQUIRED
            }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(ProductMediaSerializer(serializer.instance).data)


# product_medias/{product_media_id}
class ProductMediaDetail(APIView):

    @staticmethod
    def get(request, product_media_id):
        """
        View individual product media
        """

        product_medias = get_object_or_404(ProductMedia, pk=product_media_id)
        return Response(ProductMediaSerializer(product_medias).data)

    @staticmethod
    def patch(request, product_media_id):
        """
        Update product media
        """

        product_media = get_object_or_404(ProductMedia, pk=product_media_id)
        serializer = ProductMediaSerializerUpdate(product_media, data=request.data, context={'request': request},
                                                  partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(ProductMediaSerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, product_media_id):
        """
        Delete product media
        """

        product_media = get_object_or_404(ProductMedia, pk=product_media_id)
        if product_media.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        product_media.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
