# Generated by Django 4.1.4 on 2022-12-20 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('logo', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0)),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('servide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services1', to='apipagos.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
