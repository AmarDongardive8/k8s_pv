from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer

# Create API (POST) and Get All (GET)
class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Get Single Employee by ID
class EmployeeRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
