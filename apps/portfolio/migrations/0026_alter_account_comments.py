# Generated by Django 3.2.9 on 2022-03-03 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0025_auto_20220303_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='comments',
            field=models.TextField(blank=True, max_length=40, verbose_name='comments'),
        ),
    ]
