# Generated by Django 5.1.3 on 2025-03-18 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_remove_tbl_emergencypass_emergencypass_fromplace_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_emergencypass',
            name='emergencypass_validity',
            field=models.DateField(auto_now_add=True),
        ),
    ]
