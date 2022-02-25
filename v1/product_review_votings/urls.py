from django.urls import path
from .views.product_review_voting import ProductReviewVotingView, ProductReviewVotingDetail


urlpatterns = [

    # Product reviews
    path('product_review_votings/', ProductReviewVotingView.as_view()),
    path('product_review_votings/<product_review_voting_id>', ProductReviewVotingDetail.as_view()),

]
