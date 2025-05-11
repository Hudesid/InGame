from django.core.validators import RegexValidator
from django.db import models


class Catalog(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255, validators=[RegexValidator(
        regex=r'^[А-Яа-яЁё0-9\s\-.,!?()@#%&*]+$',
        message='Поле должно содержать только русские буквы, пробелы или дефис.'
    )])
    image = models.ImageField(upload_to="catalog_images/")
    type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Uz: {self.name_uz}, Ru: {self.name_ru}"