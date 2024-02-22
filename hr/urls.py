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
from hr.views import hrIndex, generate_payslip,payslip_list

urlpatterns = [
    path('hrindex/', hrIndex, name='hrIndex'),
    path('generate_payslip/<str:EmployeeId>/', generate_payslip, name="generate_payslip"),
    path('payslip_list/', payslip_list, name="payslip_list"),
    path('payslip_list/<str:EmployeeId>/', payslip_list, name="payslip_list")


   
]
