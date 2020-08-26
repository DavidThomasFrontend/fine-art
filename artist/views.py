from django.shortcuts import render
from .models import Artist

# Create your views here.

"""a view to show all artists including search"""

def featured(request):
    """a view to show all artists including search"""

    artist = Artist.objects.all()

    

    context = {
        'artist': artist,
    }

    return render(request, 'artist/featured.html', context)