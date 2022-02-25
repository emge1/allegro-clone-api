from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.product_questions.models.product_question import ProductQuestion
from v1.product_questions.serializers.product_question import ProductQuestionSerializer, \
    ProductQuestionCreateSerializer, ProductQuestionAnswerSerializer
from v1.products.models.product import Product
from v1.utils import constants
from v1.utils.permissions import is_customer, is_staff


# product_questions
class ProductQuestionView(APIView):

    @staticmethod
    def get(request):
        """
        List product questions
        """

        product_questions = ProductQuestion.objects.all()
        return Response(ProductQuestionSerializer(product_questions, many=True).data)

    @staticmethod
    def post(request):
        """
        Create product question
        """

        serializer = ProductQuestionCreateSerializer(data=request.data, context={'request': request})
        if not is_customer(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_MERCHANT_REQUIRED
            }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(ProductQuestionSerializer(serializer.instance).data)


# product_questions/{product_question_id}
class ProductQuestionDetail(APIView):

    @staticmethod
    def get(request, product_question_id):
        """
        View individual product question
        """

        product_question = get_object_or_404(ProductQuestion, pk=product_question_id)
        return Response(ProductQuestionSerializer(product_question).data)

    @staticmethod
    def patch(request, product_question_id):
        """
        Answer product question
        """

        product_question = get_object_or_404(ProductQuestion, pk=product_question_id)
        serializer = ProductQuestionAnswerSerializer(product_question, data=request.data, context={'request': request},
                                                     partial=True)

        product_id = serializer.data['product_id']
        product = get_object_or_404(Product, pk=product_id)

        if product.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(ProductQuestionSerializer(serializer.instance).data)

    @staticmethod
    def delete(request, product_question_id):
        """
        Delete product question
        """

        product_question = get_object_or_404(ProductQuestion, pk=product_question_id)
        if not is_staff(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_MERCHANT_REQUIRED
            }, status=status.HTTP_401_UNAUTHORIZED)
        product_question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
