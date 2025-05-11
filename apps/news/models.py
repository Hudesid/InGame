from django.core.validators import RegexValidator
from django.db import models


class New(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, validators=[RegexValidator(
        regex=r'^[А-Яа-яЁё\s-]+$',
        message='Поле должно содержать только русские буквы, пробелы или дефис.'
    )])
    description_uz = models.TextField()
    description_ru = models.TextField(validators=[RegexValidator(
        regex=r'^[А-Яа-яЁё\s-]+$',
        message='Поле должно содержать только русские буквы, пробелы или дефис.'
    )])
    youtube_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Uz: {self.title_uz}, Ru: {self.title_ru}"