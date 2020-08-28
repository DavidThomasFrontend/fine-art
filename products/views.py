from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Painting, Genre

# Create your views here.


def all_products(request):
    """a view to show all products including search"""

    
    products = Painting.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Did not enter search criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(genre__icontains=query) | Q(year__icontains=query)
            products = products.filter(queries)


    for p in products:
        print(p)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/paintings.html', context)


def genre(request, genre_slug):

    products = Painting.objects.filter(genre=genre_slug)

    context = {
        'products': products,
        'genre': genre
    }
    
    return render(request, 'products/genre.html', context)



def painting_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Painting, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/painting_detail.html', context)


def impressionism(request):
    """a view to show all products including search"""

    products = Painting.objects.all()
    

    for p in products:
        print(p)

    context = {
        'products': products,
    }

    return render(request, 'products/impressionism.html', context)


