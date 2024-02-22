from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from administrator.models import Department, EmployeeDetails, Payslip
# Create your views here.
def employeeIndex(request, EmployeeId):
    allEmpDetails = get_object_or_404(EmployeeDetails, EmployeeId=EmployeeId)
    return render(request, 'employeeindex.html', {'allEmpDetails': allEmpDetails})
