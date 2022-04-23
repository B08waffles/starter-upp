# Generated by Django 4.0.3 on 2022-04-23 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('starterupperupp', '0015_alter_transaction_associated_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='associated_company',
            field=models.ForeignKey(default='Test Company', on_delete=django.db.models.deletion.CASCADE, to='starterupperupp.company', to_field='company_name'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='associated_user',
            field=models.ForeignKey(default='b08waffles', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
