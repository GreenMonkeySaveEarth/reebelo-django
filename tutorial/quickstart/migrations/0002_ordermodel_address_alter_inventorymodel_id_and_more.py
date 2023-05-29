# Generated by Django 4.2.1 on 2023-05-28 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='address',
            field=models.CharField(default='123 Main St. SF CA', max_length=100),
        ),
        migrations.AlterField(
            model_name='inventorymodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='status',
            field=models.CharField(choices=[('processing', 'processing'), ('shipped', 'shipped'), ('delivered', 'delivered'), ('cancelled', 'cancelled')], default='processing', max_length=100),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='tracking',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='quickstart.trackingmodel'),
        ),
        migrations.AlterField(
            model_name='trackingmodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trackingmodel',
            name='tracking_company',
            field=models.CharField(choices=[('USPS', 'USPS'), ('FedEx', 'FedEx'), ('UPS', 'UPS')], default='UPS', max_length=100),
        ),
    ]
