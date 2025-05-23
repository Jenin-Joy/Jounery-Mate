# Generated by Django 5.1.3 on 2025-03-18 06:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0005_alter_tbl_driver_driver_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_number', models.CharField(max_length=50)),
                ('vehicle_count', models.CharField(max_length=50)),
                ('vehicle_photo', models.FileField(upload_to='Assets/user/photo/')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_driver')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_cabassign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabassign_date', models.CharField(max_length=50)),
                ('cabassign_amount', models.CharField(max_length=50)),
                ('cabassign_status', models.CharField(max_length=50)),
                ('cabassign_startdate', models.CharField(max_length=50)),
                ('cabassign_enddate', models.CharField(max_length=50)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_employee')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_vehicle')),
            ],
        ),
    ]
