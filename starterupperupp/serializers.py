from rest_framework_json_api import serializers

from starterupperupp.models import Company, Transaction

from django.contrib.auth.models import User


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id', 'company_name', 'company_slogan', 'created_date', 'last_updated_date'
        )


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            'id', 'created_date', 'last_updated_date', 'associated_company_id', 'approved',
            'amount', 'type_of_contribution', 'associated_user_id'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'password', 'last_login', 'is_superuser', 'username', 'last_name',
            'email', 'is_staff', 'is_active', 'date_joined', 'first_name'
        )
