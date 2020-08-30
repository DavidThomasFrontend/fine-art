from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Nothing to see here!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51GulB3LxmzpAngybEgKPLf06k5Dxx24TZOAy4L0ZjZAI7ytSnexCLmCyeQxn9FHA0dP6mjXLYoKuPvvdCpfoBfGv00sHpWDAGF',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)