from django.core.validators import RegexValidator
from django.db import models


class Banner(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255, validators=[RegexValidator(
        regex=r'^[А-Яа-яЁё0-9\s\-.,!?()@#%&*]+$',
        message='Поле должно содержать только русские буквы, пробелы или дефис.'
    )])
    description_uz = models.TextField()
    description_ru = models.TextField(validators=[RegexValidator(
        regex=r'^[А-Яа-яЁё0-9\s\-.,!?()@#%&*]+$',
        message='Поле должно содержать только русские буквы, пробелы или дефис.'
    )])
    image = models.ImageField(upload_to="banners_images/")
    url = models.URLField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Uz: {self.name_uz}, Ru: {self.name_ru}"