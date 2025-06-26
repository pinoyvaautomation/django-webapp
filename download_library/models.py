from django.db import models # type: ignore

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255, blank=True)
    telephone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = "Categorys"
        verbose_name_plural = "Categories"


class File(models.Model):
    title = models.CharField(max_length=200)
    upload = models.FileField(upload_to='files/')
    category = models.ForeignKey(Category, related_name='files', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    customers = models.ManyToManyField(Customer, related_name='files', blank=True)

    def __str__(self):
        return self.title

