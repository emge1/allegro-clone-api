from django.urls import path
from .views.category import CategoryView, CategoryDetail
from v1.subcategories.views.subcategory import SubcategoryView
from v1.products.views.product import ProductView


urlpatterns = [

    # Categories
    path('categories/', CategoryView.as_view()),
    path('categories/<category_id>', CategoryDetail.as_view()),
    path('categories/<category_id>/subcategories/', SubcategoryView.as_view(), name='subcategories-list'),
    path('categories/<category_id>/products/', ProductView.as_view(), name='products-list'),
]
