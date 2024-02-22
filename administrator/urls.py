"""
URL configuration for hrms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from administrator.views import adminIndex, add_employee, view_all_employees, remove_employee, filter_employee
urlpatterns = [
    path('admindex/', adminIndex, name='adminIndex'),
    path('addemployee/', add_employee, name='add_employee'),
    path('view_all_emp', view_all_employees, name='view_all_employees'),
    path('remove_emp/',remove_employee, name="remove_employee"),
    path('remove_employee/<str:EmployeeId>/', remove_employee, name='remove_employee'),
    path('filter_emp/', filter_employee, name='filter_employee'),
    
]
