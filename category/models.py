from django.db import models

# Create your models here.
class Category(models.Model):
    nama_barang = models.CharField(max_length=255)
    kategori_barang = models.CharField(max_length=255)
    
    def __str__(self):
        return self.kategori_barang