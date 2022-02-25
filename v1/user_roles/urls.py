from django.urls import path
from .views.administrator import AdministratorView
from .views.staff import StaffView, StaffDetail


urlpatterns = [

    # Administrators
    path('administrators/', AdministratorView.as_view()),

    # Moderators
    path('staffs', StaffView.as_view()),
    path('staffs/<staff_id>', StaffDetail.as_view()),

]
