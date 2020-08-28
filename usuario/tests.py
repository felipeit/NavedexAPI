from rest_framework.test import APITestCase
from rest_framework import status


class AccountTestCase(APITestCase):
    def setUp(self):
        data ={
            "email":"admin@admin.com",
            "password":"admin"
        }
        self.client.post('/api/create_user/', data)
        
        self.client.login(**data)

    def test_root(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_projetos(self):
        response = self.client.get('/api/projetos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_projetos_create(self):
        data = {
            "name":"Projeto Test"
        }
        response = self.client.post('/api/projetos/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_usuario(self):
        response = self.client.get('/api/usuario/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_usuario_create(self):
        data = {
            "name": "Test",
            "birthdate": "2020-08-27",
            "admission_date": "2020-08-27",
            "job_role": "Develop",
            "projetos": 1
        }
        response = self.client.post('/api/projetos/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)