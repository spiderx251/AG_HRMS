from django.shortcuts import render, HttpResponse, get_object_or_404
from Administrator.models import Employee_details
from datetime import datetime 
from django.db.models import Q
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

def remove_emp(request, employee_id = 0):
    if employee_id:
        try:
            emp_to_be_removed = Employee_details.objects.get(id=employee_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Successfully Removed")
        except:
            return HttpResponse("Please Enter a valid EmployeeId")

    employes = Employee_details.objects.all()
    context = {'employes':employes}
    
    return render(request, 'remove_emp.html', context)

    

def filter_emp(request):
    if request.method=="POST":
        name = request.POST['name']
        EmployeeId = request.POST['EmployeeId']
        Department = request.POST['Department']

        employes = Employee_details.objects.all()

        if name:
            employes = employes.filter(Q(FirstName__icontains = name) | Q(LastName__icontains = name))
        if Department:
            employes = employes.filter(Department__name=Department)
        if EmployeeId:
            employes = employes.filter(EmployeeId__name=EmployeeId)
        
        context = {'employes':employes}

        return render(request, "view_all_emp.html", context) 
    
    elif request.method=="GET":
        return render(request, 'filter_emp.html')
    
    else:
        return HttpResponse("An Exception occured")



    return render(request, 'filter_emp.html')


def view_all_emp(request):
    employes = Employee_details.objects.all()
    context = {'employes':employes}
    print(context)
    return render(request, 'view_all_emp.html', context)