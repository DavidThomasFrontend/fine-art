from django.shortcuts import render, get_object_or_404
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



    def paintings_detail(request):
        """a view to show individual paintings"""

    product = get_object_or_404(Painting, pk=product_id)

    for p in products:
        print(p)

    context = {
        'products': products,
    }

    return render(request, 'products/paintings.html', context)
