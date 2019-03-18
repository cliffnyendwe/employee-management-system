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
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Employees
from .serializer import EmployeesSerializer

def all_employees(request,*args,**kwargs):
    users = Employees.objects.filter().order_by('-id')
    paginator = Paginator(users,10) 
    page = request.GET.get('page')
    

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request,'employees/all_employees.html',{'users':users})


# show employee detail
class EmployeeDetailView(DetailView):
    template_name = 'employees/employee_detail.html'

    def get_queryset(self):
        unique = Employees.objects.filter(id=self.kwargs['pk'])
        return unique

    
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
        context['title'] = 'New Employee'
        return context

# update employee information except salary
class EmployeeUpdateView(UpdateView):
    form_class = UpdateEmployeeForm
    model = Employees
    template_name = 'employees/employee_update.html'

    def get_queryset(self):
        unique = Employees.objects.filter(id=self.kwargs['pk'])
        return unique

    def get_context_data(self, **kwargs):
        context = super(EmployeeUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Update Employee'
        return context



# delete employee if not connected to a contract
class EmployeeDeleteView(DeleteView):
    template_name = 'employees/employee_detail.html'

    def post(self, *args, **kwargs):
        unique = Employees.objects.filter(id=self.kwargs['pk'], freeze=False).first()
        contract_status = unique.contract
        if contract_status is None or contract_status == '':
            unique.delete()
            return redirect(reverse('employees:all'))
        else:
            unique.freeze = True
            unique.save()
            messages.error(self.request, 'you can not delete this employee because he has a contract')
            return redirect(reverse('employees:all'))

class EmployeesList(APIView):
    def get(self, request, format=None):
        all_merch = EmloyeesMerch.objects.all()
        serializers = EmployeesSerializer(all_merch, many=True)
        return Response(serializers.data)







