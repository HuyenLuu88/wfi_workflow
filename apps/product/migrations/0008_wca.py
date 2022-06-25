# Generated by Django 3.2.9 on 2022-03-10 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0007_delete_wca'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secid', models.IntegerField()),
                ('isin', models.CharField(max_length=12, null=True)),
                ('uscode', models.CharField(max_length=9)),
                ('sedol', models.CharField(max_length=7)),
                ('issuername', models.CharField(max_length=70)),
                ('sectycd', models.CharField(max_length=3)),
                ('bondtype', models.CharField(max_length=10)),
                ('securitydesc', models.CharField(max_length=70)),
                ('statusflag', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name_plural': 'WCA',
            },
        ),
    ]