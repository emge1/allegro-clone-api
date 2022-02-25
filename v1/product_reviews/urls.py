from django.urls import path
from .views.product_review import ProductReviewView, ProductReviewDetail


urlpatterns = [

    # Product reviews
    path('product_reviews/', ProductReviewView.as_view()),
    path('product_reviews/<product_review_id>', ProductReviewDetail.as_view()),

]
