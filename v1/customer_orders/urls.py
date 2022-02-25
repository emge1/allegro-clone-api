from django.urls import path
from .views.customer_order import CustomerOrderView, CustomerOrderDetail


urlpatterns = [

    # Customer orders
    path('customer_orders/', CustomerOrderView.as_view()),
    path('customer_orders/<customer_order_id>', CustomerOrderDetail.as_view()),

]