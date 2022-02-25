from django.urls import path
from .views.product_detail import ProductDetailView, ProductDetailDetail


urlpatterns = [

    # Product details
    path('product_details/', ProductDetailView.as_view()),
    path('product_details/<product_detail_id>', ProductDetailDetail.as_view()),

]