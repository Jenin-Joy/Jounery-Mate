# Generated by Django 5.2 on 2025-04-14 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_tbl_rentvehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_complaint',
            name='complaint_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
