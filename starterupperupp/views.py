from django.shortcuts import render
from django.contrib.auth.models import User
from starterupperupp.models import Company, Transaction
from starterupperupp.serializers import CompanySerializer, TransactionSerializer, UserSerializer
from rest_framework import viewsets


# Views handle the HTTP requests for our models

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
