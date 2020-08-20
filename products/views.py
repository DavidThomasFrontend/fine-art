from django.shortcuts import render
from .models import Painting

# Create your views here.


def all_products(request):
    """a view to show all products including search"""

    products = Painting.objects.all()

    for p in products:
        print(p)

    context = {
        'products': products,
    }

    return render(request, 'products/paintings.html', context)
