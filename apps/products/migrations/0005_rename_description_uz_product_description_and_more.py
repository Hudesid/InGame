# Generated by Django 5.2 on 2025-05-12 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description_uz',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name_uz',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name_ru',
        ),
    ]
