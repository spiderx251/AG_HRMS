from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name
    

class Employee_details(models.Model):
    FirstName     = models.CharField(max_length=30, null=False)
    LastName      = models.CharField(max_length=30)
    FatherName    = models.CharField(max_length=30)
    EmployeeId    = models.CharField(max_length=30)  
    Department    = models.ForeignKey(Department, on_delete=models.CASCADE)
    Designation   = models.CharField(max_length=30)
    JoiningDate   = models.DateField(max_length=8)
    phoneNumber   = models.CharField(max_length=10)
    Mail_id       = models.EmailField(max_length = 254)
   # DOB           = models.DateField()
    Salary        = models.BigIntegerField()
    PAN           = models.CharField(max_length=10) 
    UAN           = models.BigIntegerField()
    BankAccount   = models.BigIntegerField()
    Image         = models.ImageField(upload_to='static/images', null='true', blank='true')


    def __str__(self):
        return self.FirstName



    

