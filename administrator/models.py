from django.db import models
from django.utils import timezone
class Department(models.Model):
    name = models.CharField(max_length=30, null=False)
    def __str__(self):
        return self.name



class EmployeeDetails(models.Model):
    EmployeeId   = models.CharField(max_length=30, null=False, primary_key=True)
    Firstname    = models.CharField(max_length=30, null=False)
    Lastname     = models.CharField(max_length=30, null=False)
    Department   = models.ForeignKey(Department, on_delete=models.CASCADE)
    Designation  = models.CharField(max_length=30, null=False)
    JoiningDate  = models.DateField()
    DateofBirth  = models.DateField()
    phoneNumber  = models.CharField(max_length=13)
    Mail_Id      = models.EmailField(max_length=254)
    PAN          = models.CharField(max_length=15)
    UAN          = models.BigIntegerField()
    BankAccount  = models.BigIntegerField()
    Salary       = models.FloatField(null=False)
    BasicPay     = models.FloatField(null=False)
    Image        = models.ImageField(upload_to='static/images', null=True, blank=True)
    
    def __str__(self):
        return self.EmployeeId 
    


class Payslip(models.Model):
    EmployeeId    = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE, primary_key=True)
    BasicPay      = models.FloatField(null=False)
    HRA =models.FloatField(null=False)
    DA = models.FloatField(null=False)
    SpecialAllowance = models.FloatField(null=False)
    GrossSalary = models.FloatField(null=False)
    PF_Contribution = models.FloatField()
    ProfessionalTax = models.FloatField(null=False)
    OtherDeductions = models.FloatField(null=False)
    GrossDeductions = models.FloatField(null=False)
    NetSalary       = models.FloatField(null=False)
    Datetime        = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.EmployeeId