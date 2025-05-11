from django.core.validators import RegexValidator
from django.db import models


class TradeIn(models.Model):
    class StatusChoice(models.TextChoices):
        Process = "process", "Process"
        Success = "success", "Success"
        Cancelled = "cancelled", "Cancelled"

    name = models.CharField(max_length=255)
    phone = models.CharField(
        max_length=50,
        validators=[RegexValidator(
            regex=r'^\+\d+$',
            message="Phone number must start with '+' followed by digits."
        )]
    )
    telegram_nik = models.CharField(
        max_length=32,
        validators=[RegexValidator(
            regex=r'^@[\w]{4,31}$',
            message="Telegram nickname must start with '@' and be 5–32 characters long."
        )]
    )
    config = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=StatusChoice.choices, default=StatusChoice.Process)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}"


    def save(self, *args, **kwargs):
        self.name = self.name[0].upper() + self.name[1:]
        super().save(*args, **kwargs)