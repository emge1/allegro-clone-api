from django.urls import path
from .views.product_variant_items import ProductVariantItemView, ProductVariantItemDetail


urlpatterns = [

    # Product variant items
    path('product_variant_items/', ProductVariantItemView.as_view()),
    path('product_variant_items/<product_variant_item_id>', ProductVariantItemDetail.as_view()),

]