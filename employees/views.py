from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    View,
)
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages

from .forms import (
    AddEmployeeForm,
    UpdateEmployeeForm,

)
from .models import Employees


# show all employees
class AllEmployeesView(ListView):
    template_name = 'employees/all_employees.html'
    # template_name = 'employees/all_employees_table.html'

    def get_queryset(self):
        qs = Employees.objects.filter().order_by('-id')
        return qs

    def get_context_data(self, **kwargs):
        context = super(AllEmployeesView, self).get_context_data(**kwargs)
        context['title'] = 'All Employees'
        return context


# show employee detail
class EmployeeDetailView(DetailView):
    template_name = 'employees/employee_detail.html'

    def get_queryset(self):
        qs = Employees.objects.filter(id=self.kwargs['pk'])
        return qs

    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Employee'
        return context


# add new employee
class AddEmployeeView(CreateView):
    form_class = AddEmployeeForm
    template_name = 'employees/add_new_employee.html'

    def get_context_data(self, **kwargs):
        context = super(AddEmployeeView, self).get_context_data(**kwargs)
        context['title'] = 'Add Employee'
        return context


# update employee information except salary
class EmployeeUpdateView(UpdateView):
    form_class = UpdateEmployeeForm
    model = Employees
    template_name = 'employees/employee_update.html'

    def get_queryset(self):
        qs = Employees.objects.filter(id=self.kwargs['pk'])
        return qs

    def get_context_data(self, **kwargs):
        context = super(EmployeeUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Update Employee'
        return context


# delete employee if not connected to a job
class EmployeeDeleteView(DeleteView):
    template_name = 'employees/employee_detail.html'

    def post(self, *args, **kwargs):
        qs = Employees.objects.filter(id=self.kwargs['pk'])
        job_status = qs.job
        if job_status is None or job_status == '':
            qs.delete()
            return redirect(reverse('employees:all'))
        else:
            qs.freeze = True
            qs.save()
            messages.error(self.request, 'you can not delete this employee because he has a job')
            return redirect(reverse('employees:all'))




