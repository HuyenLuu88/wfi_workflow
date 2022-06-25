# Generated by Django 3.2.9 on 2021-12-19 21:24

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20211219_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='office',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='company_role', chained_model_field='company_role', null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.office'),
        ),
    ]
