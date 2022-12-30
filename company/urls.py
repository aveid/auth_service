from django.urls import path

from company import views

urlpatterns = [
    path("departments/<int:pk>/", views.EmployeeDepartmentAPIView.as_view()),
]