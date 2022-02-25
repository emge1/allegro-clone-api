from django.urls import path
from .views.product_variant import ProductVariantView, ProductVariantDetail


urlpatterns = [

    # Product variants
    path('product_variants/', ProductVariantView.as_view()),
    path('product_variants/<product_variant_id>', ProductVariantDetail.as_view()),

]