from django.db import models

# Create your models here.


class Painting(models.Model):
    name = models.CharField(max_length=254)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    genre = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):

    genre = (
        'impressionism',
        'expressionism',
        'baroque',
        'surrealism',
    )


    def __str__(self):
        return self.name