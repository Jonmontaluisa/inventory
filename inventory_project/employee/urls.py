from django.urls import include, path
from .views import EmployeeCreate, EmployeeList, EmployeeDetail, EmployeeUpdate,EmployeeDelete

urlpatterns = [
    path('create/', EmployeeCreate.as_view()),
    path('', EmployeeList.as_view()),
    path('<int:pk>/', EmployeeDetail.as_view()),
    path('update/<int:pk>', EmployeeUpdate.as_view()),
    path('delete/<int:pk>', EmployeeDelete.as_view()),
]