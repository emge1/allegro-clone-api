from django.urls import path
from .views.product_media import ProductMediaView, ProductMediaDetail


urlpatterns = [

    # Product medias
    path('product_medias/', ProductMediaView.as_view()),
    path('product_medias/<product_media_id>', ProductMediaDetail.as_view()),

]
