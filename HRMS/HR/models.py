from django.db import models

# Create your models here.
class Payslip(models.Model):
    Basic_Pay = models.FloatField(null=False, default=0)
    DA       = models.FloatField(null=False, default=0)
    HRA      = models.FloatField(null=False, default=0)
    Special_Allowance = models.FloatField() 
    Gross_Salary = models.FloatField(null=False, default=0)
    PF_Contribution = models.FloatField(null=False, default=0)
    Professional_TAx = models.FloatField(null=False, default=0)
    Other_Deductions = models.FloatField()
    Gross_Deductions = models.FloatField(null=False, default=0)
    Net_Salary = models.FloatField(null=False, default=0)

