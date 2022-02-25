from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.products.models.product import Product
from v1.products.serializers.product import ProductSerializer, ProductSerializerCreate, ProductSerializerUpdate
from v1.utils import constants
from v1.utils.permissions import is_merchant


# products
class ProductView(APIView):

    @staticmethod
    def get(request):
        """
        List products
        """

        products = Product.objects.all()
        return Response(ProductSerializer(products, many=True).data)

    @staticmethod
    def post(request):
        """
        Create product
        """

        serializer = ProductSerializerCreate(data=request.data, context={'request': request})
        if not is_merchant(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_MERCHANT_REQUIRED
            }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(ProductSerializer(serializer.instance).data)


# products/{product_id}
class ProductDetail(APIView):

    @staticmethod
    def get(request, product_id):
        """
        View individual product
        """

        subcategories = get_object_or_404(Product, pk=product_id)
        return Response(ProductSerializer(subcategories).data)

    @staticmethod
    def patch(request, product_id):
        """
        Update product
        """

        product = get_object_or_404(Product, pk=product_id)
        serializer = ProductSerializerUpdate(product, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(ProductSerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, product_id):
        """
        Delete product
        """

        product = get_object_or_404(Product, pk=product_id)
        if product.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
