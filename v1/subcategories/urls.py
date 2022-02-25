from django.urls import path
from .views.subcategory import SubcategoryView, SubcategoryDetail


urlpatterns = [

    # Subcategories
    path('subcategories/', SubcategoryView.as_view()),
    path('subcategories/<subcategory_id>', SubcategoryDetail.as_view()),

]
