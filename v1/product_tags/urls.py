from django.urls import path
from .views.product_tag import ProductTagView, ProductTagDetail


urlpatterns = [

    # Product tags
    path('product_variants/', ProductTagView.as_view()),
    path('product_variants/<product_variant_id>', ProductTagDetail.as_view()),

]