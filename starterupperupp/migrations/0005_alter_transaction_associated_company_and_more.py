# Generated by Django 4.0.3 on 2022-04-22 01:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('starterupperupp', '0004_alter_transaction_associated_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='associated_company',
            field=models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, to='starterupperupp.company', to_field='company_name'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='associated_user',
            field=models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
