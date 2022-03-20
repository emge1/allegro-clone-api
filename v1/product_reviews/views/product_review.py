from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.product_reviews.models.product_review import ProductReview
from v1.product_reviews.serializers.product_review import ProductReviewSerializer, ProductReviewSerializerCreate, \
    ProductReviewSerializerUpdate
from v1.utils import constants
from v1.utils.permissions import is_customer, is_staff


# product_reviews
class ProductReviewView(APIView):

    @staticmethod
    def get(request):
        """
        List product reviews
        """

        product_reviews = ProductReview.objects.all()
        return Response(ProductReviewSerializer(product_reviews, many=True).data)

    @staticmethod
    def post(request):
        """
        Create product review
        """

        serializer = ProductReviewSerializerCreate(data=request.data, context={'request': request})
        if not is_customer(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_MERCHANT_REQUIRED
            }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(ProductReviewSerializer(serializer.instance).data)


# product_reviews/{product_review_id}
class ProductReviewDetail(APIView):

    @staticmethod
    def get(request, product_review_id):
        """
        View individual product review
        """

        product_review = get_object_or_404(ProductReview, pk=product_review_id)
        return Response(ProductReviewSerializer(product_review).data)

    @staticmethod
    def patch(request, product_review_id):
        """
        Update product review
        """

        product_review = get_object_or_404(ProductReview, pk=product_review_id)
        serializer = ProductReviewSerializerUpdate(product_review, data=request.data, context={'request': request},
                                                   partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(ProductReviewSerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, product_review_id):
        """
        Delete product review
        """

        product_review = get_object_or_404(ProductReview, pk=product_review_id)
        if not is_staff(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_STAFF_REQUIRED
            }, status=status.HTTP_401_UNAUTHORIZED)
        product_review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
