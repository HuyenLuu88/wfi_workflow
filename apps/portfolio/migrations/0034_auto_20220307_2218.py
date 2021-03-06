# Generated by Django 3.2.9 on 2022-03-07 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0033_alter_account_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uscode',
            name='account',
        ),
        migrations.RemoveField(
            model_name='identifier',
            name='code_id',
        ),
        migrations.AddField(
            model_name='account',
            name='isin_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='sedol_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='uscode_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='ISIN',
        ),
        migrations.DeleteModel(
            name='USCODE',
        ),
    ]
