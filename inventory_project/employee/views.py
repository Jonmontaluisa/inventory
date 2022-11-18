from django.shortcuts import render
from .models import Employee
from rest_framework import generics
from .serializers import EmployeeSerializer


class EmployeeCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Employee.objects.all(),
    serializer_class = EmployeeSerializer