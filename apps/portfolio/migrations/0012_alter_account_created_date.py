# Generated by Django 3.2.9 on 2022-01-11 11:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_auto_20220111_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
