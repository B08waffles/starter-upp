import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from starterupperupp import views
from starterupperupp.models import Company, Transaction
from starterupperupp.serializers import (CompanySerializer,
                                         TransactionSerializer, UserSerializer)


class TestApi(APITestCase):

    def setUp(self):
        ''' pre-populate the django test database so that we can test '''
        self.user_1 = User.objects.create(
            id='1', username='test-1', password='dwqdf@2d')
        self.user_2 = User.objects.create(
            id='2', username='test-2', password='dwsdvf@2d')
        self.company_1 = Company.objects.create(
            id='1', company_name='ywqehd', company_slogan='wefvjwj')
        self.company_2 = Company.objects.create(
            id='2', company_name='ewqehd', company_slogan='wsdgjwj')
        self.transaction_1 = Transaction.objects.create(
            amount='40', type_of_contribution='HW', associated_company=self.company_1, associated_user=self.user_1)
        self.transaction_2 = Transaction.objects.create(
            amount='40', type_of_contribution='HW', associated_company=self.company_2, associated_user=self.user_2)

    def test_get_transactions(self):
        ''' Test GET all transactions and test TransactionSerializer '''
        url = reverse('transaction-list')
        response = self.client.get(url)
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, response.data)

    def test_get_a_transaction(self):
        ''' Test to see if we can get a particular transaction '''
        url = reverse('transaction-detail', args=(self.transaction_1.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_companys(self):
        ''' Test GET all companys and test CompanySerializer '''
        url = reverse('company-list')
        response = self.client.get(url)
        companys = Company.objects.all()
        serializer = CompanySerializer(companys, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, response.data)

    def test_get_a_company(self):
        ''' Test to see if we can get a particular company '''
        url = reverse('company-detail', args=(self.company_1.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_users(self):
        """ Test GET all users and test UserSerializer """
        url = reverse('user-list')
        response = self.client.get(url)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, response.data)

    def test_get_a_user(self):
        ''' Test to see if we can get a particular user '''
        url = reverse('user-detail', args=(self.user_1.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        """ Test if we can create a user """
        url = reverse('user-list')
        data = {
            "data": {
                "type": "User",
                "id": '3',
                "attributes": {
                    "username": "JimmyBarnes",
                    "password": "Strong_password123",
                }
            }
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_company(self):
        """ Test if we can create a company """
        url = reverse('company-list')
        data = {
            "data": {
                "type": "Company",
                "attributes": {
                    "company_name": "AussieTeamB",
                    "company_slogan": "Yeah Mate",
                }
            }
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_transaction(self):
        """ Test if we can create a transaction """
        url = reverse('transaction-list')
        data = {
            "data": {
                "type": "Transaction",
                "id": "3",
                "attributes": {
                    "created_date": "2022-04-04T05:24:06.096551Z",
                    "last_updated_date": "2022-04-04T05:24:06.096621Z",
                    "approved": "false",
                    "amount": "42.0",
                    "type_of_contribution": "HW"
                },
                "relationships": {
                    "associated_company": {
                        "data": {
                            "type": "Company",
                            "id": "2"
                        }
                    },
                    "associated_user": {
                        "data": {
                            "type": "User",
                            "id": "2"
                        }
                    }
                }
            }
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
