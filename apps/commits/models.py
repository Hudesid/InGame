from django.core.validators import RegexValidator
from django.db import models
from apps.products.models import Product
from apps.desktops.models import Desktop


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ProductComment(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    username = models.CharField(max_length=255)
    comment = models.TextField()
    image = models.ImageField(upload_to="product_comments_photo/")
    rating = models.IntegerField()


    def __str__(self):
        return self.username


    def save(self, *args, **kwargs):
        self.username = self.username[0].upper() + self.username[1:]
        super().save(*args, **kwargs)


class DesktopComment(BaseModel):
    desktop = models.ForeignKey(Desktop, on_delete=models.CASCADE, related_name="comments")
    username = models.CharField(max_length=255)
    comment = models.TextField()
    image = models.ImageField(upload_to="product_comments_photo/")
    rating = models.IntegerField()


    def __str__(self):
        return self.username


    def save(self, *args, **kwargs):
        self.username = self.username[0].upper() + self.username[1:]
        super().save(*args, **kwargs)


class Comment(BaseModel):
    username = models.CharField(max_length=255)
    comment_uz = models.TextField(default="No comment")
    comment_ru = models.TextField(default="Без комментариев", validators=[RegexValidator(
        regex=r'^[А-Яа-яЁё0-9\s\-.,!?()@#%&*]+$',
        message='Поле должно содержать только русские буквы, пробелы или дефис.'
    )])
    description_uz = models.TextField(default="No description")
    description_ru = models.TextField(default="Нет описания", validators=[RegexValidator(
        regex=r'^[А-Яа-яЁё0-9\s\-.,!?()@#%&*]+$',
        message='Поле должно содержать только русские буквы, пробелы или дефис.'
    )])
    image = models.ImageField(upload_to="comment_photos/")
    video = models.FileField(upload_to="comment_videos/")


    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.username = self.username[0].upper() + self.username[1:]
        super().save(*args, **kwargs)