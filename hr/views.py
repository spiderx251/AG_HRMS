from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from administrator.models import EmployeeDetails, Payslip
# Create your views here.

def hrIndex(request):
    return render(request, 'hrindex.html')


def generate_payslip(request, EmployeeId):
    employee = get_object_or_404(EmployeeDetails, EmployeeId=EmployeeId)
    BasicPay = employee.BasicPay 
    BankAccount = employee.BankAccount
    HRA = 0.1 * BasicPay 
    DA  = 0.2 * BasicPay
    SpecialAllowance = 0 
    GrossSalary = BasicPay + HRA + DA + SpecialAllowance 
    PF_Contribution = 0.12 * BasicPay
    ProfessionalTax = 200 
    OtherDeductions = 0 
    GrossDeductions = PF_Contribution + ProfessionalTax + OtherDeductions 
    NetSalary = GrossSalary - GrossDeductions 


    payslip = Payslip(EmployeeId=employee, BasicPay=BasicPay, HRA=HRA, DA=DA, SpecialAllowance=SpecialAllowance,
                      GrossSalary=GrossSalary, PF_Contribution=PF_Contribution, ProfessionalTax=ProfessionalTax, OtherDeductions=OtherDeductions, GrossDeductions=GrossDeductions, NetSalary=NetSalary)
    payslip.save()

    return redirect('payslip_list') 

def payslip_list(request,EmployeeId):
    #payslips = get_object_or_404(Payslip,EmployeeId=EmployeeId)
    #payslips = get_object_or_404(Payslip.objects.select_related('EmployeeId'),EmployeeId=EmployeeId)
    #payslips = Payslip.objects.filter(pk=EmployeeId).select_related('EmployeeDetails').values('EmployeeId','BasicPay').get()
    try:
        #payslips = Payslip.objects.filter(EmployeeId_id__EmployeeId=EmployeeId).select_related('EmployeeId').values('EmployeeId_id', 'BasicPay','BankAccount').get()
        payslips =  get_object_or_404(Payslip,EmployeeId=EmployeeId)
        empdetails =  get_object_or_404(EmployeeDetails,EmployeeId=EmployeeId)
       
    except Payslip.DoesNotExist:
        payslips = None

    context  = {'payslips':payslips,'empdetails':empdetails}
    return render(request, 'emppayslip.html', context)

