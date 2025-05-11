import uuid
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.utils import timezone
from datetime import timedelta


class Role(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        self.name = self.name[0].upper() + self.name[1:]
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50, validators=[RegexValidator(
        regex=r'^\+\d+$',
        message="Phone number must start with '+' followed by digits."
    )])
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, related_name="users", null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    def save(self, *args, **kwargs):
        self.first_name = self.first_name[0].upper() + self.first_name[1:]
        self.last_name = self.last_name[0].upper() + self.last_name[1:]
        super().save(*args, **kwargs)


