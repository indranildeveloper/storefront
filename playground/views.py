from django.shortcuts import render

# from django.db.models import Q, F

from store.models import Product

# Create your views here.


def say_hello(request):
    product = Product.objects.order_by("unit_price")[0]
    product = Product.objects.latest("unit_price")

    return render(request, "hello.html", {"name": "Indra", "product": product})
