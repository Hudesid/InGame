# Generated by Django 5.2 on 2025-05-10 22:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commits', '0003_alter_comment_comment_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_ru',
            field=models.TextField(default='Без комментариев', validators=[django.core.validators.RegexValidator(message='Поле должно содержать только русские буквы, пробелы или дефис.', regex='^[А-Яа-яЁё0-9\\s\\-.,!?()@#%&*]+$')]),
        ),
        migrations.AlterField(
            model_name='comment',
            name='description_ru',
            field=models.TextField(default='Нет описания', validators=[django.core.validators.RegexValidator(message='Поле должно содержать только русские буквы, пробелы или дефис.', regex='^[А-Яа-яЁё0-9\\s\\-.,!?()@#%&*]+$')]),
        ),
    ]
