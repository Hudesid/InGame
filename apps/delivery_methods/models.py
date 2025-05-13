from django.core.validators import RegexValidator
from django.db import models


class DeliveryMethod(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    estimated_delivery_time = models.IntegerField()
    logo = models.ImageField(upload_to="logos_delivery_methods/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Uz: {self.name_uz}, Ru: {self.name_ru}"


    def _validate_russian_text(self, value, field_name):
        if value:
            validator = RegexValidator(
                regex=r'^[А-Яа-яЁё0-9\s\-.,!?()@#%&*]+$',
                message=f"Поле '{field_name}' должно содержать только русские буквы, пробелы или дефис."
            )
            validator(value)


    def save(self, *args, **kwargs):
        self._validate_russian_text(self.name_ru, 'Name [ru]')

        super().save(*args, **kwargs)