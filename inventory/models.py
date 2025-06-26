from django.db import models # type: ignore
from django.utils import timezone # type: ignore
from download_library.models import Customer

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = "Categorys"
        verbose_name_plural = "Categories"
    
class Computer(models.Model):
    name = models.CharField(max_length=100)
    client = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='computers')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='computers')
    purchase_date = models.DateField()
    support_expiration_date = models.DateField()

    def is_support_active(self):
        return timezone.now().date() < self.support_expiration_date

    def __str__(self):
        return f"{self.name} ({self.client.name})"


# Create your models here.

