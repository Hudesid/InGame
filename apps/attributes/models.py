from django.core.validators import RegexValidator
from django.db import models
from apps.categories.models import Category


class Attribute(models.Model):
    type_uz = models.CharField(max_length=255)
    type_ru = models.CharField(max_length=255, validators=[RegexValidator(
        regex=r'^[А-Яа-яЁё0-9\s\-.,!?()@#%&*]+$',
        message='Поле должно содержать только русские буквы, пробелы или дефис.'
    )])
    value = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="attributes", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Uz: {self.type_uz}, Ru: {self.type_ru}"