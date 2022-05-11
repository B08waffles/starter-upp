# Generated by Django 4.0.3 on 2022-05-11 13:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starterupperupp', '0003_alter_transaction_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=55, unique=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(55)]),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_slogan',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(255)]),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.FloatField(max_length=55, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxLengthValidator(55), django.core.validators.MaxValueValidator(999999999999)]),
        ),
    ]
