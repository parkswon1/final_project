# Generated by Django 4.2.4 on 2023-09-04 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cno', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=8)),
                ('email', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=16)),
                ('birthdate', models.DateField()),
                ('gender', models.BooleanField()),
                ('password', models.CharField(max_length=20)),
                ('bookinfo', models.TextField(null=True)),
                ('boardinfo', models.TextField(null=True)),
            ],
        ),
    ]
