from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from employee.models import Employee, Position

User = get_user_model()


class TestPositionViewSet(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.positions_url = reverse('positions-list')

        cls.user = User.objects.create_user(
            username='existing',
            email='existing@user.com',
            password='existing_password')

    def test_create_parent_position(self):
        self.client.force_login(self.user)

        data = {
            "title": "CEO",
        }

        response = self.client.post(self.positions_url, data)
        response_json = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response_json.get('id'))
        self.assertEqual(response_json.get('title'), data['title'])
        self.assertEqual(response_json.get('parent'), None)

    def test_create_child_position(self):
        self.client.force_login(self.user)

        # create parent position
        parent = Position.objects.create(title='CTO')

        # create child position for test
        data = {
            "title": "SWE",
            "parent": parent.pk,
        }

        response = self.client.post(self.positions_url, data)
        response_json = response.json()
        self.assertEqual(response_json.get('title'), data['title'])
        self.assertEqual(response_json.get('parent'), parent.pk)


class TestEmployeeViewSet(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.employees_url = reverse('employees-list')

        cls.user = User.objects.create_user(
            username='existing',
            email='existing@user.com',
            password='existing_password')

        # create employee for test
        cls.cto = Position.objects.create(title='CTO')
        cls.sswe = Position.objects.create(title='Senior Software Engineer', parent=cls.cto)
        cls.swe = Position.objects.create(title='Software Engineer', parent=cls.sswe)

        Employee.objects.create(position=cls.cto, first_name='John', last_name='Doe')
        Employee.objects.create(position=cls.sswe, first_name='Mac', last_name='intosh')
        Employee.objects.create(position=cls.swe, first_name='Surf', last_name='ace')

    def test_get_all_employees(self):
        self.client.force_login(self.user)

        response = self.client.get(self.employees_url)
        response_json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_json.get('count'), 3)

    def test_get_all_employees_under_specific_position(self):
        self.client.force_login(self.user)

        response = self.client.get(self.employees_url, {'parent_position': self.cto.pk})
        response_json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_json.get('count'), 2)
        self.assertEqual(response_json.get('results')[0].get('first_name'), 'Mac')
