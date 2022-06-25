# Generated by Django 3.2.9 on 2022-01-14 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_auto_20220111_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='invalid_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='valid_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='isin',
            name='valid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='uscode',
            name='valid',
            field=models.BooleanField(default=False),
        ),
    ]