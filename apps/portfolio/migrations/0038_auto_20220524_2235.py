# Generated by Django 3.2.9 on 2022-05-24 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0037_auto_20220331_1705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='identifier',
            old_name='type',
            new_name='code_type',
        ),
        migrations.AlterModelTable(
            name='identifier',
            table='portfolio_identifier',
        ),
    ]
