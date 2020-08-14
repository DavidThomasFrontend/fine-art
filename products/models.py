from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=254)
    years = models.DecimalField(max_digits=6, decimal_places=2)
    nationality = models.CharField(max_length=254)
    bio = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    genre = models.CharField(max_length=254)

    
    
    def __str__(self):
        return self.name
