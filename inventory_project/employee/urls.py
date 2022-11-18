from django.urls import include, path
from .views import EmployeeCreate

urlpatterns = [
    path('create/', EmployeeCreate.as_view(), name='create-employee'),
]