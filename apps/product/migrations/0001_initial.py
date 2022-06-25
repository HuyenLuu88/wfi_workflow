# Generated by Django 3.2.9 on 2022-03-10 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WCA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secid', models.IntegerField()),
                ('isin', models.CharField(max_length=12)),
                ('uscode', models.CharField(max_length=9)),
                ('sedol', models.CharField(max_length=7)),
                ('issuername', models.CharField(max_length=70)),
                ('sectycd', models.CharField(max_length=3)),
                ('bondtype', models.CharField(max_length=10)),
                ('securitydesc', models.CharField(max_length=70)),
                ('statusflag', models.CharField(max_length=1)),
            ],
        ),
    ]