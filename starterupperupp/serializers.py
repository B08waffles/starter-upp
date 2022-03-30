from rest_framework_json_api import serializers
from starterupperupp.models import Company, Transaction

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'pk', 'company_name', 'company_slogan', 'created_date', 'last_updated_date'
            )

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            'pk', 'created_date', 'last_updated_date', 'associated_company', 'approved',
        'amount', 'type_of_contribution', 'associated_user'
            )        