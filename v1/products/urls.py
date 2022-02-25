from django.urls import path
from .views.product import ProductView, ProductDetail


urlpatterns = [

    # Products
    path('products/', ProductView.as_view()),
    path('products/<product_id>', ProductDetail.as_view()),

]
