from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from postgres_copy import CopyManager


# This is the model for the eployees and its field
class Employees(models.Model):

    Department_CHOICES = [
        ('employee', 'employee'),
        ('FINANCE', 'FINANCE'),
        ('HR', 'HR'),
        ('MARKETING', 'MARKETING'),
        ('OPERATIONS', 'OPERATIONS'),
        ('R%D', 'R%D'),
    ]
 
    first_name = models.CharField(max_length=60) 
    last_name = models.CharField(max_length=60)
    employee_id = models.CharField(max_length = 10, default='7584965894')
    department = models.CharField(choices=Department_CHOICES, max_length=25)
    contract = models.CharField(max_length=60, null=True)
    updated = models.DateTimeField(auto_now=True)
    phone_number = models.PositiveIntegerField(unique=True)
    email_address = models.EmailField(max_length = 60, default = '@gmail.com')
    objects = CopyManager()

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('employees:detail', kwargs={'pk': self.pk})

# This is the function for saving employee's department
def post_save_employee_receiver(sender, instance, created, *args, **kwargs):
    if created:
        unique = Employees.objects.filter(id=instance.id, department=instance.department)
        if unique.exists() and unique.count() == 1:
            employee = unique.first()
            department = employee.department
            if department == 'FINANCE':
                employee.save()
            if department == 'HR':
                employee.save()
            if department == 'MARKETING':
                employee.save()
            if department == 'OPERATIONS':
                employee.save()
            if department == 'R%D':
                employee.save()


post_save.connect(post_save_employee_receiver, sender=Employees)
