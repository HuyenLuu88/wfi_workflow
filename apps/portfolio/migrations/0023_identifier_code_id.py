# Generated by Django 3.2.9 on 2022-02-15 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0022_rename_identifier_type_identifier_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='identifier',
            name='code_id',
            field=models.IntegerField(null=True),
        ),
    ]