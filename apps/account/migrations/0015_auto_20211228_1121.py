# Generated by Django 3.2.9 on 2021-12-28 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_group_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]