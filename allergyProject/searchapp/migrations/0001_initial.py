# Generated by Django 4.2.4 on 2023-10-14 14:17

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('ano', models.AutoField(primary_key=True, serialize=False)),
                ('allergy', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'db_table': 'allergies',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('prdlstReportNo', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('prdlstNm', models.CharField(max_length=200)),
                ('rawmtrl', models.TextField()),
                ('allergy', models.TextField(null=True)),
                ('manufacture', models.CharField(max_length=200, null=True)),
                ('prdkind', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='PSimilarity',
            fields=[
                ('prdNo', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('simlist', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), null=True, size=None)),
            ],
            options={
                'db_table': 'psimilarity',
            },
        ),
        migrations.CreateModel(
            name='Recommend',
            fields=[
                ('serialno', models.AutoField(primary_key=True, serialize=False)),
                ('cno', models.IntegerField()),
                ('rno', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'recommend',
            },
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('rnum', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.BooleanField(null=True)),
                ('older', models.IntegerField(null=True)),
                ('allergy', models.TextField()),
                ('prdlstReportNo', models.CharField(max_length=20)),
                ('prdlstNm', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
            ],
            options={
                'db_table': 'userdata',
            },
        ),
    ]
