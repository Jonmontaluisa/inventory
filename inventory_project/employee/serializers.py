from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['cedula', 'name', 'last_name','email', 'date_of_birth','address','created_at']