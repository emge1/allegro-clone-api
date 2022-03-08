from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.product_transactions.models.product_transaction import ProductTransaction
from v1.product_transactions.serializers.product_transaction import ProductTransactionSerializer, \
    ProductTransactionSerializerCreate
from v1.utils import constants
from v1.utils.permissions import is_staff, is_merchant


# product_transactions
class ProductTransactionView(APIView):

    @staticmethod
    def get(request):
        """
        List product transactions
        """

        product_transactions = ProductTransaction.objects.all()
        return Response(ProductTransactionSerializer(product_transactions, many=True).data)

    @staticmethod
    def post(request):
        """
        Create product transaction
        """

        serializer = ProductTransactionSerializerCreate(data=request.data, context={'request': request})
        if not is_merchant(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_MERCHANT_REQUIRED
            }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(ProductTransactionSerializer(serializer.instance).data)


# product_transactions/{product_transaction_id}
class ProductTransactionDetail(APIView):

    @staticmethod
    def get(request, product_transaction_id):
        """
        View individual product transaction
        """

        product_transaction = get_object_or_404(ProductTransaction, pk=product_transaction_id)
        return Response(ProductTransactionSerializer(product_transaction).data)

    @staticmethod
    def delete(request, product_transaction_id):
        """
        Delete product transaction
        """

        product_transaction = get_object_or_404(ProductTransaction, pk=product_transaction_id)
        if not is_staff(request.user):
            return Response({
                constants.ERROR: constants.PERMISSION_STAFF_REQUIRED
            }, status=status.HTTP_401_UNAUTHORIZED)
        product_transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
