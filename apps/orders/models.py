from django.core.validators import RegexValidator
from django.db import models
from apps.delivery_methods.models import DeliveryMethod
from apps.desktops.models import Desktop
from apps.credits.models import Credit
from apps.products.models import Product


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Order(BaseModel):
    class StatusChoice(models.TextChoices):
        Process = "process", "Process"
        Cancelled = "cancelled", "Cancelled"
        Success = "success", "Success"

    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=50, validators=[RegexValidator(
        regex=r'^\+\d+$',
        message="Phone number must start with '+' followed by digits."
    )])
    address = models.CharField(max_length=255)
    comment = models.TextField()
    delivery_method = models.ForeignKey(DeliveryMethod, on_delete=models.SET_NULL, related_name="orders", null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=StatusChoice.choices, default=StatusChoice.Process)


    def __str__(self):
        return f"Name: {self.customer_name}, Phone number: {self.customer_phone}"


    def save(self, *args, **kwargs):
        self.customer_name = self.customer_name[0].upper() + self.customer_name[1:]
        super().save(*args, **kwargs)


class OrderDesktopItem(BaseModel):
    desktop = models.ForeignKey(Desktop, on_delete=models.PROTECT, related_name="orders")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="desktop_items")
    quantity = models.IntegerField()
    credit = models.ForeignKey(Credit, on_delete=models.PROTECT, related_name="orders")
    credit_term = models.IntegerField()
    edit_product = models.ManyToManyField(Product, related_name="desktop_item_orders", blank=True)


class OrderProductItem(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="orders")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="product_items")
    quantity = models.IntegerField()
    credit = models.ForeignKey(Credit, on_delete=models.PROTECT, related_name="product_item_orders")
    credit_term = models.IntegerField()

