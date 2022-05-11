from rest_framework_json_api import serializers

from starterupperupp.models import Company, Transaction

from django.contrib.auth.models import User


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id', 'company_name', 'company_slogan', 'created_date', 'last_updated_date'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'password', 'last_login', 'is_superuser', 'username', 'last_name',
            'email', 'is_staff', 'is_active', 'date_joined', 'first_name'
        )


class TransactionSerializer(serializers.ModelSerializer):
    # associated_company = serializers.CharField()
    # associated_user = serializers.CharField()
    class Meta:
        model = Transaction
        fields = (
            'id', 'created_date', 'last_updated_date', 'associated_company', 'approved',
            'amount', 'type_of_contribution', 'associated_user'#, 'associated_user_id',
            #'associated_company_id'
        )
        #lookup_field = 'associated_company_id'

# class PieSerializer(serializers.ModelSerializer):
#     total = serializers.SerializerMethodField()
#     user = serializers.SerializerMethodField()

#     class Meta:
#         model = Transaction
#         fields = '__all__'

#     def get_pie_chart_data(self, obj):
#         totals = {}

#         for work in transaction:
#             amount_to_be_added = 0
#         if work[obj.type_of_contribution] == obj.MI:
#             amount_to_be_added += work[obj.amount]
#         elif work[obj.type_of_contribution] == obj.HW:
#             amount_to_be_added += work["amount"] * 30
    
#         if work["associated_user"] in totals:
#             totals[work["associated_user"]] += amount_to_be_added
#         else:
#             totals[work["associated_user"]] = amount_to_be_added
#         return                 
