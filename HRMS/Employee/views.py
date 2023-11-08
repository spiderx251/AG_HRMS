from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from Administrator.models import Employee_details
# Create your views here.

def idCard(request,FirstName):
    employeeIdCard = get_object_or_404(Employee_details, FirstName=FirstName.upper())
    return render(request, 'index.html', {'employeeIdCard':employeeIdCard})
