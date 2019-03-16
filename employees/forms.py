from django import forms
from .models import Employees


class AddEmployeeForm(forms.ModelForm):
    first_name = forms.CharField(label='First name', widget=forms.TextInput(
        attrs={
            'placeholder': 'First name',
            'class': 'form-control',
        }))
  
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(
        attrs={
            'placeholder': 'Last name',
            'class': 'form-control',
        }))

    

    employee_unique_id = forms.CharField(label='Employee Unique ID', widget=forms.TextInput(
        attrs={
            'placeholder': 'Employee Unique ID',
            'class': 'form-control',
            'type': 'number',
        }))
   
    department = forms.CharField(label='Department', widget=forms.TextInput(
        attrs={
            'placeholder': 'Department',
            'class': 'form-control',
        }))
    job = forms.CharField(label='Job', required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'Job',
            'class': 'form-control',
        }))
   
  
    email = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={
            'placeholder': 'Email',
            'class': 'form-control',
            
        }))

    class Meta:
        model = Employees
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'employee_unique_id',
            'job',
            'department',
            'email',
         
        ]

    def clean_employee_unique_id(self):
        employee_unique_id = self.cleaned_data.get('employee_unique_id')
        qs = Employees.objects.filter(employee_unique_id=employee_unique_id)
        if qs.exists():
            raise forms.ValidationError('This Employee is already Added before!')
        if int(employee_unique_id) <= 9:
            raise forms.ValidationError('Employee Unique ID must be bigger than 10!')
        if len(str(employee_unique_id)) < 10 or len(str(employee_unique_id)) > 15:
            raise forms.ValidationError('Employee Unique ID must be more than 10 values')
        return int(employee_unique_id)


class UpdateEmployeeForm(forms.ModelForm):
    first_name = forms.CharField(label='First name', widget=forms.TextInput(
        attrs={
            'placeholder': 'First name',
            'class': 'form-control',
        }))
  
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(
        attrs={
            'placeholder': 'Last name',
            'class': 'form-control',
        }))

    employee_unique_id = forms.CharField(label='Employee Unique ID', widget=forms.TextInput(
        attrs={
            'placeholder': 'Employee Unique ID',
            'class': 'form-control',
            'type': 'number',
        }))
   
    department = forms.CharField(label='Department', widget=forms.TextInput(
        attrs={
            'placeholder': 'Department',
            'class': 'form-control',
        }))
    job = forms.CharField(label='Job', required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'Job',
            'class': 'form-control',
        }))
   
  
    email = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={
            'placeholder': 'Email',
            'class': 'form-control',
            
        }))

    class Meta:
        model = Employees
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'employee_unique_id',
            'job',
            'department',
            'email',
         
        ]

    def clean_employee_unique_id(self):
        employee_unique_id = self.cleaned_data.get('employee_unique_id')
        if int(employee_unique_id) <= 9:
            raise forms.ValidationError('Employee Unique ID must be bigger than 10!')
        if len(str(employee_unique_id)) < 10 or len(str(employee_unique_id)) > 15:
            raise forms.ValidationError('Employee Unique ID must be more than 10 values')
        return int(employee_unique_id)


