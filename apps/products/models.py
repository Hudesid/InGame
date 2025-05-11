from django.core.validators import RegexValidator
from django.db import models
from apps.attributes.models import Attribute
from apps.statuses.models import Status
from apps.product_types.models import ProductType
from apps.categories.models import Category
from apps.brands.models import Brand
from django.utils.text import slugify


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(BaseModel):
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
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="products", null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="products")
    discount = models.IntegerField(default=0)
    attributes = models.ManyToManyField(Attribute, related_name="products")
    statuses = models.ManyToManyField(Status, related_name="products")
    type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, related_name="products", null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)


    def __str__(self):
        return f"Uz: {self.name_uz}. Ru: {self.name_ru}."


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_uz)
        super().save(*args, **kwargs)


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products_images/")


    def __str__(self):
        return self.product.name_uz