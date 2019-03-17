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

from .forms import (AddEmployeeForm, UpdateEmployeeForm,)
from .models import Employees


# show all employees
class AllEmployeesView(ListView):
    template_name = 'employees/all_employees.html'
    # template_name = 'employees/all_employees_table.html'

    def get_queryset(self):
        co = Employees.objects.filter().order_by('-id')
        return co

    def get_context_data(self, **kwargs):
        context = super(AllEmployeesView, self).get_context_data(**kwargs)
        context['title'] = 'All Employees'
        return context


# show employee detail
class EmployeeDetailView(DetailView):
    template_name = 'employees/employee_detail.html'

    def get_queryset(self):
        co = Employees.objects.filter(id=self.kwargs['pk'])
        return co

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
        co = Employees.objects.filter(id=self.kwargs['pk'])
        return co

    def get_context_data(self, **kwargs):
        context = super(EmployeeUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Update Employee'
        return context


# delete employee if not connected to a contract
class EmployeeDeleteView(DeleteView):
    template_name = 'employees/employee_detail.html'

    def post(self, *args, **kwargs):
        co = Employees.objects.filter(id=self.kwargs['pk'], freeze=False).first()
        contract_status = co.contract
        if contract_status is None or contract_status == '':
            co.delete()
            return redirect(reverse('employees:all'))
        else:
            co.freeze = True
            co.save()
            messages.error(self.request, 'you can not delete this employee because he has a contract')
            return redirect(reverse('employees:all'))


def index(request):
    user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'list.html', { 'users': users })





