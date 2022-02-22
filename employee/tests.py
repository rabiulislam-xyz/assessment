from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from model_bakery import baker


User = get_user_model()


class TestUserViewSet(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.positions_url = reverse('positions-list')
        cls.employees_list_url = reverse('positions-list')

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
        parent = baker.make('employee.Position', title='CTO')

        # create child position for test
        data = {
            "title": "SWE",
            "parent": parent.pk,
        }

        response = self.client.post(self.positions_url, data)
        response_json = response.json()
        self.assertEqual(response_json.get('title'), data['title'])
        self.assertEqual(response_json.get('parent'), parent.pk)

