# Generated by Django 5.2 on 2025-05-07 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_verify_email',
        ),
    ]
