from django.core.validators import RegexValidator
from django.db import models


class DeliveryMethod(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255, validators=[RegexValidator(
        regex=r'^[А-Яа-яЁё\s-]+$',
        message='Поле должно содержать только русские буквы, пробелы или дефис.'
    )])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    estimated_delivery_time = models.IntegerField()
    logo = models.ImageField(upload_to="logos_delivery_methods/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Uz: {self.name_uz}, Ru: {self.name_ru}"