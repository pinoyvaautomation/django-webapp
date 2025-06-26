#from django.db import models

# Create your models here.
from django.db import models # type: ignore
from ckeditor.fields import RichTextField # type: ignore

class Category(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = "Categorys"
        verbose_name_plural = "Categories"

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField() # Use CKEditor for the content field
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
