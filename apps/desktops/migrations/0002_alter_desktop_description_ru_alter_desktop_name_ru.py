# Generated by Django 5.2 on 2025-05-07 10:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desktops', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desktop',
            name='description_ru',
            field=models.TextField(validators=[django.core.validators.RegexValidator(message='Поле должно содержать только русские буквы, пробелы или дефис.', regex='^[А-Яа-яЁё\\s-]+$')]),
        ),
        migrations.AlterField(
            model_name='desktop',
            name='name_ru',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Поле должно содержать только русские буквы, пробелы или дефис.', regex='^[А-Яа-яЁё\\s-]+$')]),
        ),
    ]
