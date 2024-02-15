# Generated by Django 5.0.2 on 2024-02-09 06:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userpass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='username')),
                ('password', models.IntegerField(unique=True, verbose_name='password')),
                ('usertype', models.CharField(max_length=50, verbose_name='usertype')),
            ],
            options={
                'db_table': 'userpass',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='techname')),
                ('phone', models.IntegerField(unique=True, verbose_name='phone')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='email')),
                ('departmant', models.CharField(max_length=50, verbose_name='departmant')),
                ('passid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.userpass', verbose_name='passid')),
            ],
            options={
                'db_table': 'Teacher',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='stdtname')),
                ('phone', models.IntegerField(unique=True, verbose_name='phone')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='email')),
                ('departmant', models.CharField(max_length=50, verbose_name='departmant')),
                ('passid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.userpass', verbose_name='passid')),
            ],
            options={
                'db_table': 'Student',
            },
        ),
    ]
