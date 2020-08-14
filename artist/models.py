from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=254)
    nationality = models.CharField(max_length=254)
    bio = models.TextField()
    genre = models.CharField(max_length=254)
    year = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return self.name
   