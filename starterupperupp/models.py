from django.contrib.auth.models import User
from django.db import models

# Models are created here, this is for use with sqlite3, django's built in ORM and database system


class Company(models.Model):
    company_name = models.CharField(max_length=255)
    company_slogan = models.TextField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

# the function in the models, the text after `def`, is dictating what the admin panel sees from the model


class Transaction(models.Model):
    CHOICES = (
        ('HW', 'Hours worked'),
        ('MI', 'Money invested'),
    )
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)
    associated_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    amount = models.FloatField()
    type_of_contribution = models.CharField(max_length=25, choices=CHOICES)
    associated_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __int__(self):
        return self.pk
