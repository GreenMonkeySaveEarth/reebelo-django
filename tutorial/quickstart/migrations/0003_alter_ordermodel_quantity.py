# Generated by Django 4.2.1 on 2023-05-29 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_ordermodel_address_ordermodel_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
