from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, first_name=None, last_name=None, password=None, email=None, role=None, phone=None, **extra_fields):
        if not first_name:
            raise ValueError("First name is required.")
        if not last_name:
            raise ValueError("Last name is required.")
        if not email:
            raise ValueError("Email is required.")
        if not role:
            raise ValueError("Role is required")
        if not phone:
            raise ValueError("Phone number is required.")

        email = self.normalize_email(email)
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            role=role,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, first_name=None, last_name=None, password=None, email=None, role=None, phone=None, **extra_fields):
        from .models import Role
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        role = Role.objects.filter(name="Admin").first()
        return self.create_user(first_name, last_name, password, email, role, phone, **extra_fields)