from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.product_details.models.product_detail import ProductDetail
from v1.product_details.serializers.product_detail import ProductDetailsSerializer, ProductDetailSerializerCreate, \
    ProductDetailSerializerUpdate
from v1.utils import constants
from v1.utils.permissions import is_merchant


# product_details
class ProductDetailView(APIView):

    @staticmethod
    def get(request):
        """
        List product details
        """

        product_details = ProductDetail.objects.all()
        return Response(ProductDetailsSerializer(product_details, many=True).data)

    @staticmethod
    def post(request):
        """
        Create product details
        """

        serializer = ProductDetailSerializerCreate(data=request.data, context={'request': request})
        if not is_merchant(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_MERCHANT_REQUIRED
            }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(ProductDetailsSerializer(serializer.instance).data)


# product_details/{product_detail_id}
class ProductDetailDetail(APIView):

    @staticmethod
    def get(request, product_detail_id):
        """
        View individual product detail
        """

        product_details = get_object_or_404(ProductDetail, pk=product_detail_id)
        return Response(ProductDetailsSerializer(product_details).data)

    @staticmethod
    def patch(request, product_detail_id):
        """
        Update product detail
        """

        product_detail = get_object_or_404(ProductDetail, pk=product_detail_id)
        serializer = ProductDetailSerializerUpdate(product_detail, data=request.data, context={'request': request},
                                                   partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(ProductDetailsSerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, product_detail_id):
        """
        Delete product detail
        """

        product_detail = get_object_or_404(ProductDetail, pk=product_detail_id)
        if product_detail.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        product_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
