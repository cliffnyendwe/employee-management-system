from django.test import TestCase
from django.core.urlresolvers import reverse


class TestCalls(TestCase):

    def test_new_employee(self):
        response = self.client.post(reverse('employees:add'), {
                                    'first_name': 'Cliff',
                                    'last_name': 'Nyendwe',
                                    'phone_number': '0710750000'
                                    'employee_unique_id':'123456789101112',
                                    'date_of_birth': 'cliffnyendwe2018@gmail.com',
                                    'department': [1],
                                   
                                    }
                                    )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'employees/add_new_employee.html')
        self.assertContains(response, 'developer')

