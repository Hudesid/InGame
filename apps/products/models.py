from django.core.validators import RegexValidator
from django.db import models, transaction
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
    name = models.CharField(max_length=255)
    description = models.TextField()
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


    def _validate_russian_text(self, value, field_name):
        if value:
            validator = RegexValidator(
                regex=r'^[А-Яа-яЁё0-9\s\-.,!?()@#%&*]+$',
                message=f"Поле '{field_name}' должно содержать только русские буквы, пробелы или дефис."
            )
            validator(value)


    def save(self, *args, **kwargs):
        with transaction.atomic():
            is_new = self._state.adding

            self._validate_russian_text(self.name_ru, 'Name [ru]')
            self._validate_russian_text(self.description_ru, 'Description [ru]')

            if not self.slug:
                base_name = self.name_uz if self.name_uz else self.name_ru
                if base_name:
                    self.slug = slugify(base_name)

            temp_attributes = list(self.attributes.all()) if not is_new else []
            temp_statuses = list(self.statuses.all()) if not is_new else []

            super().save(*args, **kwargs)

            if is_new:
                if hasattr(self, 'attributes') and temp_attributes:
                    self.attributes.set(temp_attributes)
                if hasattr(self, 'statuses') and temp_statuses:
                    self.statuses.set(temp_statuses)



class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products_images/")


    def __str__(self):
        return self.product.name