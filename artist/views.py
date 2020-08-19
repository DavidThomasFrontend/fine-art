from django.shortcuts import render
from .models import Artist

# Create your views here.

"""a view to show all products including search"""

def artists(request):
    return render(request, 'artist/artists.html', context)