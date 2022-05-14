# Generated by Django 4.0.3 on 2022-05-11 13:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starterupperupp', '0004_alter_company_company_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='type_of_contribution',
            field=models.CharField(choices=[('HW', 'Hours worked'), ('MI', 'Money invested')], max_length=2, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(2)]),
        ),
    ]