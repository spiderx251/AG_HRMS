from django import forms 
from administrator.models import Payslip 

class PayslipForm(forms.ModelForm):
    class Meta:
        model = Payslip 
        files = '__all__'
