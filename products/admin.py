from django.contrib import admin
from .models import Painting
# Register your models here.


class PaintingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'year',
        'price',
        'image',
    )



admin.site.register(Painting, PaintingAdmin)
