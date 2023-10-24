from django.db import models
from category.models import Category

# # Create your models here.

class Blog(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    blog_date = models.DateField()
    kategori_barang = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title