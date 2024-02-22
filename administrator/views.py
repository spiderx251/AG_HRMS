from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse 
from django.shortcuts import get_object_or_404 
from administrator.models import EmployeeDetails, Payslip
from administrator.forms import EmployeeDetailsForm
from django.db.models import Q
from django.urls import reverse
# Create your views here.
def adminIndex(request):
    return render(request, 'adminIndex.html')

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_all_employees') 
    else:
        form = EmployeeDetailsForm()
        return render(request, 'add_employee.html', {'form':form})
    
    # return HttpResponse("Employee Successfully added")
    


def view_all_employees(request):
    employes = EmployeeDetails.objects.all()
    context  = {'employes':employes}
    return render(request, 'view_all_employees.html', context)


def remove_employee(request, EmployeeId=None):
    if EmployeeId:
        try:
            emp_to_be_removed = EmployeeDetails.objects.get(EmployeeId=EmployeeId)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Successfully Removed")
        except EmployeeDetails.DoesNotExist:
            return HttpResponse("Employee Not Found")
        
    else:
        employes = EmployeeDetails.objects.all()
        context = {'employes':employes}
        return render(request, 'remove_employee.html', context)

def filter_employee(request):
    if request.method =="POST":
        name = request.POST['name']
        EmployeeId = request.POST['EmployeeId']  
        Department = request.POST['Department'] 

        employes = EmployeeDetails.objects.all() 

        if name:
            employes = employes.filter(Q(Firstname__icontains = name) | Q(Lastname__icontains = name))
        if Department:
            employes = employes.filter(Department__name = Department)
        if EmployeeId:
            employes = employes.filter(EmployeeId__name = EmployeeId)


        context = {'employes':employes}
        
        return render(request, 'view_all_employees.html', context)
    
    elif request.method =="GET":
        return render(request, 'filter_employee.html')
    else:
        return HttpResponse("An Exception Occured")
    

