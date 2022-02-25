from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.product_review_votings.models.product_review_voting import ProductReviewVoting
from v1.product_review_votings.serializers.product_review_voting import ProductReviewVotingSerializer, \
    ProductReviewVotingSerializerCreate, ProductReviewVotingSerializerUpdate
from v1.utils import constants
from v1.utils.permissions import is_customer, is_staff


# product_review_votings
class ProductReviewVotingView(APIView):

    @staticmethod
    def get(request):
        """
        List product review votings
        """

        product_review_votings = ProductReviewVoting.objects.all()
        return Response(ProductReviewVotingSerializer(product_review_votings, many=True).data)

    @staticmethod
    def post(request):
        """
        Create product review voting
        """

        serializer = ProductReviewVotingSerializerCreate(data=request.data, context={'request': request})
        if not is_customer(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_MERCHANT_REQUIRED
            }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(ProductReviewVotingSerializer(serializer.instance).data)


# product_review_votings/{product_review_voting_id}
class ProductReviewVotingDetail(APIView):

    @staticmethod
    def get(request, product_review_voting_id):
        """
        View individual product review voting
        """

        product_review_voting = get_object_or_404(ProductReviewVoting, pk=product_review_voting_id)
        return Response(ProductReviewVotingSerializer(product_review_voting).data)

    @staticmethod
    def patch(request, product_review_voting_id):
        """
        Update product review voting
        """

        product_review_voting = get_object_or_404(ProductReviewVoting, pk=product_review_voting_id)
        serializer = ProductReviewVotingSerializerUpdate(product_review_voting, data=request.data,
                                                         context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(ProductReviewVotingSerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, product_review_voting_id):
        """
        Delete product review voting
        """

        product_review_voting = get_object_or_404(ProductReviewVoting, pk=product_review_voting_id)
        if not is_staff(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_MERCHANT_REQUIRED
            }, status=status.HTTP_401_UNAUTHORIZED)
        product_review_voting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
