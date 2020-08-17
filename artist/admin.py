from django.contrib import admin
from .models import Artist
# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'nationality',
        'birth',
        'death',
        'genre',
        'bio',
        'image',

    )



admin.site.register(Artist, ArtistAdmin)
