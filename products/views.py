from django.shortcuts import render
from .models import Painting

# Create your views here.

"""a view to show all products including search"""

products = Painting.objects.all()

context = {
    'products': products,
}

def all_products(request):
    return render(request, 'products/paintings.html', context)