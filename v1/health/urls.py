from django.urls import path
from .views import HealthView
from .views import ReadyzView

urlpatterns = [
    path("healthz", HealthView.as_view()),
    path("readyz", ReadyzView.as_view()),
]
