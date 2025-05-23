# Generated by Django 5.2 on 2025-05-03 12:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must start with '+998' and be followed by 9 digits.", regex='^\\+998\\d{9}$')])),
                ('operator_commit', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('process', 'Process'), ('cancelled', 'Cancelled'), ('success', 'Success')], default='process', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
