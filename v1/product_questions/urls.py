from django.urls import path
from .views.product_question import ProductQuestionView, ProductQuestionDetail


urlpatterns = [

    # Product questions
    path('product_questions/', ProductQuestionView.as_view()),
    path('product_questions/<product_question_id>', ProductQuestionDetail.as_view()),

]