from django import forms 
from administrator.models import EmployeeDetails 


class EmployeeDetailsForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetails
        fields = '__all__'