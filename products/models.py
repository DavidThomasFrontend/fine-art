from django.db import models

# Create your models here.


class Painting(models.Model):
    name = models.CharField(max_length=254)
    year = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    

    
    
    def __str__(self):
        return self.name
