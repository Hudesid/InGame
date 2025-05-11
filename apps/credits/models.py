from django.db import models


class Credit(models.Model):
    name = models.CharField(max_length=255)
    bank_credit = models.DecimalField(max_digits=10, decimal_places=2)
    logo = models.ImageField(upload_to="credits_logo/")
    months = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name