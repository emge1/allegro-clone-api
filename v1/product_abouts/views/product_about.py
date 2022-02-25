from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.product_abouts.models.product_about import ProductAbout
from v1.product_abouts.serializers.product_about import ProductAboutSerializer, ProductAboutSerializerCreate, \
    ProductAboutSerializerUpdate
from v1.utils import constants
from v1.utils.permissions import is_merchant


# product_abouts
class ProductAboutView(APIView):

    @staticmethod
    def get(request):
        """
        List product abouts
        """

        product_abouts = ProductAbout.objects.all()
        return Response(ProductAboutSerializer(product_abouts, many=True).data)

    @staticmethod
    def post(request):
        """
        Create product about
        """

        serializer = ProductAboutSerializerCreate(data=request.data, context={'request': request})
        if not is_merchant(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_MERCHANT_REQUIRED
            }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(ProductAboutSerializer(serializer.instance).data)


# product_abouts/{product_about_id}
class ProductAboutDetail(APIView):

    @staticmethod
    def get(request, product_about_id):
        """
        View individual product about
        """

        product_abouts = get_object_or_404(ProductAbout, pk=product_about_id)
        return Response(ProductAboutSerializer(product_abouts).data)

    @staticmethod
    def patch(request, product_about_id):
        """
        Update product about
        """

        product_about = get_object_or_404(ProductAbout, pk=product_about_id)
        serializer = ProductAboutSerializerUpdate(product_about, data=request.data, context={'request': request},
                                                  partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(ProductAboutSerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, product_about_id):
        """
        Delete product about
        """

        product_about = get_object_or_404(ProductAbout, pk=product_about_id)
        if product_about.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        product_about.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
