from django.core.validators import RegexValidator
from django.db import models
from django.utils.text import slugify
from apps.categories.models import Category
from apps.products.models import Product
from apps.statuses.models import Status
from apps.desktop_types.models import DesktopType
from apps.attributes.models import Attribute


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Desktop(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="desktops")
    type = models.CharField(max_length=255)
    desktop_types = models.ManyToManyField(DesktopType, related_name="desktops")
    attributes = models.ManyToManyField(Attribute, related_name="desktops", blank=True)
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
    price = models.DecimalField(max_digits=10, decimal_places=2)
    products = models.ManyToManyField(Product, related_name="desktops")
    statuses = models.ManyToManyField(Status, related_name="desktops")
    slug = models.SlugField(unique=True, blank=True)
    

    def __str__(self):
        return f"Uz: {self.name_uz}, Ru: {self.name_ru}"


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_uz)
        super().save(*args, **kwargs)


class DesktopImage(BaseModel):
    image = models.ImageField(upload_to="desktops_images/")
    desktop = models.ForeignKey(Desktop, on_delete=models.CASCADE, related_name="images")





