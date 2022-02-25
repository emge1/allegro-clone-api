from django.urls import path
from .views.order_delivery_status import OrderDeliveryStatusView, OrderDeliveryStatusDetail


urlpatterns = [

    # Order delivery status
    path('order_delivery_status/', OrderDeliveryStatusView.as_view()),
    path('order_delivery_status/<order_delivery_status_id>', OrderDeliveryStatusDetail.as_view()),

]
