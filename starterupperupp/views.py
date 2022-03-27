from django.shortcuts import render
from starterupperupp.models import Company, Transaction
from starterupperupp.serializers import CompanySerializer, TransactionSerializer
from rest_framework import viewsets 


# Views handle the HTTP requests for our models

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer    
