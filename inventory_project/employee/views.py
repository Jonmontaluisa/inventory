from django.shortcuts import render

from django.shortcuts import render
from .models import Employee
from rest_framework import generics
from .serializers import EmployeeSerializer

class EmployeeCreate(generics.CreateAPIView):
    queryset = Employee.objects.all(),
    serializer_class = EmployeeSerializer