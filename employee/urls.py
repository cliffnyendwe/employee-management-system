from django.conf.urls import url, include
from django.contrib import admin
from employees.views import all_employees

from django.conf import settings
from django.conf.urls.static import static

# from employees.views import AllEmployeesView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^employees/', include('employees.urls', namespace='employees')),
    # url(r'^$', AllEmployeesView.as_view(), name='main_home'),
    url(r'^$', all_employees, name='all_employees')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

