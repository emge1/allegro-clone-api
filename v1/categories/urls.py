from django.urls import path
from .views.category import CategoryView, CategoryDetail


urlpatterns = [

    # Categories
    path('categories/', CategoryView.as_view()),
    path('categories/<category_id>', CategoryDetail.as_view()),

]
