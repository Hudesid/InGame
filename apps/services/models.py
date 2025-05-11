from django.core.validators import RegexValidator
from django.db import models


class Service(models.Model):
    class StatusChoice(models.TextChoices):
        Process = "process", "Process"
        Cancelled = "cancelled", "Cancelled"
        Success = "success", "Success"

    class TypeChoice(models.TextChoices):
        Admin = 'admin', 'Admin'
        Customer = 'customer', 'Customer'

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50, validators=[RegexValidator(
        regex=r'^\+\d+$',
        message="Phone number must start with '+' followed by digits."
    )])
    type = models.CharField(max_length=20, choices=TypeChoice.choices, default=TypeChoice.Customer)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=StatusChoice.choices, default=StatusChoice.Process)
    other_services = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Customer name: {self.name}, Phone: {self.phone}"


    def save(self, *args, **kwargs):
        self.name = self.name[0].upper() + self.name[1:]
        super().save(*args, **kwargs)


class ServiceName(models.Model):
    name = models.CharField(max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="services")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name