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
            # 'type': 'number',
        }))
   
    department = forms.CharField(label='Department', widget=forms.TextInput(
        attrs={
            'placeholder': 'Department',
            'class': 'form-control',
        }))
    contract = forms.CharField(label='Contract', required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'Contract',
            'class': 'form-control',
        }))
   
  
    email = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={
            'placeholder': 'Email',
            'class': 'form-control',
            
        }))

    class Meta:
        model = Employees
        fields = '__all__'

    def clean_employee_unique_id(self):
        employee_unique_id = self.cleaned_data.get('employee_unique_id')
        unique = Employees.objects.filter(employee_unique_id=employee_unique_id)
        if unique.exists():
            raise forms.ValidationError('This Employee exist')
        if int(employee_unique_id) <= 9:
            raise forms.ValidationError('Employee Unique ID must be bigger than 10!')
        if len(str(employee_unique_id)) < 10 or len(str(employee_unique_id)) > 15:
            raise forms.ValidationError('Employee Unique ID must be more than 10 values')
        return int(employee_unique_id)

    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        unique = Employees.objects.filter(email=email)
        if unique.exists():
            raise forms.ValidationError('This Employee is already Added before!')
        return int(email)
        



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
    contract = forms.CharField(label='Contract', required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'Contract',
            'class': 'form-control',
        }))
   
    email = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={
            'placeholder': 'Email',
            'class': 'form-control',
            
        }))

    class Meta:
        model = Employees
        fields = '__all__'
          

    def clean_employee_unique_id(self):
        employee_unique_id = self.cleaned_data.get('employee_unique_id')
        if int(employee_unique_id) <= 9:
            raise forms.ValidationError('Employee Unique ID must be bigger than 10!')
        if len(str(employee_unique_id)) < 10 or len(str(employee_unique_id)) > 15:
            raise forms.ValidationError('Employee Unique ID must be more than 10 digits')
        return int(employee_unique_id)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        unique = Employees.objects.filter(email=email)
        if unique.exists():
            raise forms.ValidationError('This Employee is already Added before!')
        return int(email)






