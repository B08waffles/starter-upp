import json
import time
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from django.test import Client
from rest_framework.permissions import AllowAny
from starterupperupp import views
from rest_framework.authtoken.views import obtain_auth_token
from starterupperupp.models import Company, Transaction
from starterupperupp.serializers import (CompanySerializer,
                                         TransactionSerializer, UserSerializer)


class TestApi(APITestCase):
    #permission_classes = (AllowAny,)

    def setUp(self):
        ''' pre-populate the django test database so that we can test '''
        self.user_1 = User.objects.create_user(
            id='1', username='test-1', password='[dwqdf@2d')
        Token.objects.create(user=self.user_1)
        self.user_2 = User.objects.create_user(
            id='2', username='test-2', password='dwsdvf@2d', first_name='Joel', last_name='Bidios', email='joel@gmail.com')

        token, created = Token.objects.get_or_create(user=self.user_1)
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)

        token, created = Token.objects.get_or_create(user=self.user_2)
        self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)

        self.company_1 = Company.objects.create(
            id='1', company_name='ywqehd', company_slogan='wefvjwj')
        self.company_2 = Company.objects.create(
            id='2', company_name='ewqehd', company_slogan='wsdgjwj')
        self.transaction_1 = Transaction.objects.create(
            amount='40', type_of_contribution='HW', associated_company=self.company_1, associated_user=self.user_1)
        self.transaction_2 = Transaction.objects.create(
            amount='40', type_of_contribution='HW', associated_company=self.company_2, associated_user=self.user_2)

    def test_get_transactions(self):
        time.sleep(1)
        ''' Test GET all transactions and test TransactionSerializer '''
        token = User.objects.get(username='test-1').auth_token.key
        url = reverse('transaction-list')
        response = self.client.get(
            url, **{'HTTP_AUTHORIZATION': f"Token {token}"})
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, response.data)

    def test_get_a_transaction(self):
        time.sleep(1)
        ''' Test to see if we can get a particular transaction '''
        token = User.objects.get(username='test-1').auth_token.key
        url = reverse('transaction-detail', args=(self.transaction_1.id,))
        response = self.client.get(
            url, **{'HTTP_AUTHORIZATION': f"Token {token}"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_companys(self):
        time.sleep(1)
        ''' Test GET all companys and test CompanySerializer '''
        token = User.objects.get(username='test-1').auth_token.key
        url = reverse('company-list')
        response = self.client.get(
            url, **{'HTTP_AUTHORIZATION': f"Token {token}"})
        companys = Company.objects.all()
        serializer = CompanySerializer(companys, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, response.data)

    def test_get_a_company(self):
        time.sleep(1)
        ''' Test to see if we can get a particular company '''
        token = User.objects.get(username='test-1').auth_token.key
        url = reverse('company-detail', args=(self.company_1.id,))
        response = self.client.get(
            url, **{'HTTP_AUTHORIZATION': f"Token {token}"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_a_user(self):
        time.sleep(1)
        ''' Test to see if we can get a particular user '''
        token = User.objects.get(username='test-1').auth_token.key
        url = reverse('user-detail', args=(self.user_1.id,))
        response = self.client.get(
            url, **{'HTTP_AUTHORIZATION': f"Token {token}"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        time.sleep(1)
        """ Test if we can create a user """
        token = User.objects.get(username='test-1').auth_token.key
        url = reverse('user-list')
        data = {
            "username": "JimmyBarnes",
            "password": "Strong_password123",
            "email": "strongemail@gmail.com",
        }
        response = self.client.post(
            url, data, **{'HTTP_AUTHORIZATION': f"Token {token}"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_company(self):
        time.sleep(1)
        """ Test if we can create a company """
        token = User.objects.get(username='test-1').auth_token.key
        url = reverse('company-list')
        data = {
            "company_name": "AussieTeamB",
            "company_slogan": "Yeah Mate",
        }

        response = self.client.post(
            url, data, **{'HTTP_AUTHORIZATION': f"Token {token}"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_transaction(self):
        time.sleep(1)
        """ Test if we can create a transaction """
        token = User.objects.get(username='test-1').auth_token.key
        url = reverse('transaction-list')
        data = {
            "amount": "45",
            "type_of_contribution": "HW",
            "associated_company": "ewqehd",
            "associated_user": "test-1"
        }

        response = self.client.post(
            url, data, **{'HTTP_AUTHORIZATION': f"Token {token}"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Test to see if we can register a new user on the token generating endpoint
    # def test_register_user(self):
    #     time.sleep(1)
    #     url = reverse(views.signup)
    #     data = {
    #         "username": "bigBoiJimmybig",
    #         "email": "bigboi123@gmail.com",
    #         "password": "TheOneAndOnly123!2%$32",
    #         "first_name": "mateymate",
    #         "last_name": "Yeahnahyeah"
    #     }
    #     print(data)
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_users(self):
        time.sleep(1)
        """ Test GET all users and test UserSerializer """
        token = User.objects.get(username='test-1').auth_token.key
        url = reverse('user-list')
        response = self.client.get(
            url, **{'HTTP_AUTHORIZATION': f"Token {token}"})
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, response.data)

    def test_login_user(self):
        time.sleep(1)
        """ Test to see if we can login  """
        url = reverse(obtain_auth_token)
        data = {
            "username": "test-2",
            "password": "dwsdvf@2d",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
