# Generated by Django 5.1.3 on 2025-04-07 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_alter_tbl_passrequest_passrequest_date_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_rentvehicle',
        ),
    ]
