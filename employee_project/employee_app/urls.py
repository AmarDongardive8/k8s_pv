from django.urls import path
from .views import EmployeeListCreateAPIView, EmployeeRetrieveAPIView

urlpatterns = [
    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveAPIView.as_view(), name='employee-detail'),
]
