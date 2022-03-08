from django.urls import path
from .views.product_transaction import ProductTransactionView, ProductTransactionDetail


urlpatterns = [

    # Product transactions
    path('product_transactions/', ProductTransactionView.as_view()),
    path('product_transactions/<product_transaction_id>', ProductTransactionDetail.as_view()),

]
