from django.urls import path
from .views.product_about import ProductAboutView, ProductAboutDetail


urlpatterns = [

    # Product abouts
    path('product_abouts/', ProductAboutView.as_view()),
    path('product_abouts/<product_about_id>', ProductAboutDetail.as_view()),

]