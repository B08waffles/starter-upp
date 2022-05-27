from django.contrib import admin
from .models import Transaction
from .models import Company
from .models import PayRate
# Register your models here.
admin.site.register(Transaction)
admin.site.register(Company)
admin.site.register(PayRate)
admin.site.site_header = 'STARTER UPP'
admin.site.site_title = 'STARTER UPP'