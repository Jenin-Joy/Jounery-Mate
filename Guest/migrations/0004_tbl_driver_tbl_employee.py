# Generated by Django 5.1.3 on 2025-03-08 05:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0010_tbl_vehicle'),
        ('Guest', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=50)),
                ('driver_email', models.CharField(max_length=50)),
                ('driver_contact', models.CharField(max_length=50)),
                ('driver_address', models.CharField(max_length=100)),
                ('driver_photo', models.FileField(upload_to='Assets/user/photo/')),
                ('driver_proof', models.FileField(upload_to='Assets/user/photo/')),
                ('driver_license', models.FileField(upload_to='Assets/user/photo/')),
                ('driver_password', models.CharField(max_length=50)),
                ('driver_status', models.CharField(max_length=50)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=50)),
                ('employee_email', models.CharField(max_length=50)),
                ('employee_contact', models.CharField(max_length=50)),
                ('employee_address', models.CharField(max_length=100)),
                ('employee_photo', models.FileField(upload_to='Assets/user/photo/')),
                ('employee_proof', models.FileField(upload_to='Assets/user/photo/')),
                ('employee_password', models.CharField(max_length=50)),
                ('employee_status', models.CharField(max_length=50)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
                ('transportationtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_transportationtype')),
            ],
        ),
    ]
