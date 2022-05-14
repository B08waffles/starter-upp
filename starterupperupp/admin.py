from django.contrib import admin
from .models import Transaction
from .models import Company
# Register your models here.
admin.site.register(Transaction)
admin.site.register(Company)
admin.site.site_header = 'STARTER UPP'
admin.site.site_title = 'STARTER UPP'