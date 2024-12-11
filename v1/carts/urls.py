from django.urls import path
from .views.cart import CartView
from v1.products.views.product import ProductView


urlpatterns = [

    # Cart
    path('cart/', CartView.as_view()),
]
