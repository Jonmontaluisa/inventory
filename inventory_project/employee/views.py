from .models import Employee
from rest_framework import generics
from .serializers import EmployeeSerializer


class EmployeeCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
class EmployeeList(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class EmployeeDetail(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class EmployeeDelete(generics.RetrieveDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()