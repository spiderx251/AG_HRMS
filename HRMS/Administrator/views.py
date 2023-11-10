from django.shortcuts import render, HttpResponse
from Administrator.models import Employee_details
from datetime import datetime
# Create your views here.

def index(request):
    return render(request, 'emp_index.html')


def add_emp(request):
    if request.method=="POST":
        FirstName     = request.POST['FirstName']
        LastName      = request.POST['LastName']
        FatherName    = request.POST['FatherName']
        EmployeeId    = request.POST['EmployeeId'] 
        Department    = request.POST['Department']
        Designation   = request.POST['Designation']
        JoiningDate   = request.POST['JoiningDate']
        phoneNumber   = request.POST['phoneNumber']
        Mail_id       = request.POST['Mail_id']
        Salary        = request.POST['Salary']
        PAN           = request.POST['PAN']
        UAN           = request.POST['UAN']
        BankAccount   = request.POST['BankAccount']
        Image         = request.POST['Image']


        new_emp = Employee_details(FirstName=FirstName, LastName=LastName, FatherName=FatherName, EmployeeId=EmployeeId, Department_id=Department,
                                   Designation=Designation, JoiningDate=JoiningDate, phoneNumber=phoneNumber, Mail_id=Mail_id, Salary=Salary, PAN=PAN, UAN=UAN,
                                    BankAccount=BankAccount, Image=Image )
        new_emp.save()
        return HttpResponse('Employee added Successfully')
    elif request.method=="GET":
        return render(request, 'add_emp.html')
    else:
        return HttpResponse('An Exception Occured! Employee Has Not Been Added')

def remove_emp(request):
    return render(request, 'remove_emp.html')

def filter_emp(request):
    return render(request, 'filter_emp.html')


def view_all_emp(request):
    employes = Employee_details.objects.all()
    context = {'employes':employes}
    print(context)
    return render(request, 'view_all_emp.html', context)