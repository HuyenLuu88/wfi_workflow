# Generated by Django 3.2.9 on 2022-01-11 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20220111_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
