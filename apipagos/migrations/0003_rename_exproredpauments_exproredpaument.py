# Generated by Django 4.1.4 on 2022-12-20 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apipagos', '0002_paymentuser_expiration_date_exproredpauments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExproredPauments',
            new_name='ExproredPaument',
        ),
    ]
