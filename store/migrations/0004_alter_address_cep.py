# Generated by Django 4.1.2 on 2023-09-26 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_address_customeraddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='cep',
            field=models.CharField(max_length=15),
        ),
    ]