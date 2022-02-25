from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.product_variants.models.product_variant import ProductVariant
from v1.product_variants.serializers.product_variant import ProductVariantSerializer, ProductVariantSerializerCreate, \
    ProductVariantSerializerUpdate
from v1.utils import constants
from v1.utils.permissions import is_merchant


# product_variants
class ProductVariantView(APIView):

    @staticmethod
    def get(request):
        """
        List product variants
        """

        product_variants = ProductVariant.objects.all()
        return Response(ProductVariantSerializer(product_variants, many=True).data)

    @staticmethod
    def post(request):
        """
        Create product variant
        """

        serializer = ProductVariantSerializerCreate(data=request.data, context={'request': request})
        if not is_merchant(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_MERCHANT_REQUIRED
            }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(ProductVariantSerializer(serializer.instance).data)


# product_variants/{product_variant_id}
class ProductVariantDetail(APIView):

    @staticmethod
    def get(request, product_variant_id):
        """
        View individual product variant
        """

        product_variant = get_object_or_404(ProductVariant, pk=product_variant_id)
        return Response(ProductVariantSerializer(product_variant).data)

    @staticmethod
    def patch(request, product_variant_id):
        """
        Update product variant
        """

        product_variant = get_object_or_404(ProductVariant, pk=product_variant_id)
        serializer = ProductVariantSerializerUpdate(product_variant, data=request.data, context={'request': request},
                                                    partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(ProductVariantSerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, product_variant_id):
        """
        Delete product variant
        """

        product_variant = get_object_or_404(ProductVariant, pk=product_variant_id)
        if product_variant.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        product_variant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
