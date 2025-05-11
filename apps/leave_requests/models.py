from django.core.validators import RegexValidator
from django.db import models


class LeaveRequest(models.Model):
    class StatusChoice(models.TextChoices):
        Process = "process", "Process"
        Cancelled = "cancelled", "Cancelled"
        Success = "success", "Success"

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50, validators=[RegexValidator(
        regex=r'^\+\d+$',
        message="Phone number must start with '+' followed by digits."
    )])
    operator_commit = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=StatusChoice.choices, default=StatusChoice.Process)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'Name: {self.name}, Phone: {self.phone}'


    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super().save(*args, **kwargs)