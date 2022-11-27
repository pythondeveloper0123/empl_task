from django.urls import path
from .views import *

urlpatterns = [
    path('emp/', EmployeeAPI.as_view()),
    path('emp/<int:pk>/', EmployeeAPIView.as_view()),
]
