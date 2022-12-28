from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.RegisterUserAPIView.as_view()),
    path("activate/<str:activation_code>/",
         views.ActivateAccountView.as_view(), name="activate_account"),
]