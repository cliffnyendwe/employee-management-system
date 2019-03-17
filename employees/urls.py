from django.conf.urls import url

from .views import (
    AddEmployeeView,
    # AllEmployeesView,
    EmployeeDetailView,
    EmployeeUpdateView,
    EmployeeDeleteView,
    
    # UploadView,
)

urlpatterns = [
    url(r'^add/$', AddEmployeeView.as_view(), name='add'), # urls for adding new employee
    
    # url(r'^$', AllEmployeesView.as_view(), name='all'), # urls for showing all employees
    url(r'^(?P<pk>\d+)/$', EmployeeDetailView.as_view(), name='detail'), # urls for employees details
    url(r'^(?P<pk>\d+)/update/$', EmployeeUpdateView.as_view(), name='update'), # urls for updating employees
    url(r'^(?P<pk>\d+)/delete/$', EmployeeDeleteView.as_view(), name='delete'), # urls for deleting employee
    # url(r'^(?P<pk>\d+)/upload/$', UploadView.as_view(), name='upload'),  # urls for uploading csv file
]
