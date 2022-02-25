from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.product_variant_items.models.product_variant_items import ProductVariantItem
from v1.product_variant_items.serializers.product_variant_items import ProductVariantItemSerializer, \
    ProductVariantItemSerializerCreate, ProductVariantItemSerializerUpdate
from v1.utils import constants
from v1.utils.permissions import is_merchant


# product_variant_items
class ProductVariantItemView(APIView):

    @staticmethod
    def get(request):
        """
        List product variant items
        """

        product_variant_items = ProductVariantItem.objects.all()
        return Response(ProductVariantItemSerializer(product_variant_items, many=True).data)

    @staticmethod
    def post(request):
        """
        Create product variant item
        """

        serializer = ProductVariantItemSerializerCreate(data=request.data, context={'request': request})
        if not is_merchant(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_MERCHANT_REQUIRED
            }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(ProductVariantItemSerializer(serializer.instance).data)


# product_variant_items/{product_variant_item_id}
class ProductVariantItemDetail(APIView):

    @staticmethod
    def get(request, product_variant_item_id):
        """
        View individual product variant item
        """

        product_variant_item = get_object_or_404(ProductVariantItem, pk=product_variant_item_id)
        return Response(ProductVariantItemSerializer(product_variant_item).data)

    @staticmethod
    def patch(request, product_variant_item_id):
        """
        Update product variant item
        """

        product_variant_item = get_object_or_404(ProductVariantItem, pk=product_variant_item_id)
        serializer = ProductVariantItemSerializerUpdate(product_variant_item, data=request.data,
                                                        context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(ProductVariantItemSerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, product_variant_item_id):
        """
        Delete product variant item
        """

        product_variant_item = get_object_or_404(ProductVariantItem, pk=product_variant_item_id)
        if product_variant_item.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        product_variant_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
