
from rest_framework import status
from rest_framework.test import APITestCase


class ApiTestCase(APITestCase):

    def test_employees_status_code(self):

        response = self.client.get('/employees/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_departaments_status_code(self):
        response = self.client.get('/departaments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
