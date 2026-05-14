from django.shortcuts import render
from django.db.models import Q

from store.models import Product

# Create your views here.


def say_hello(request):
    query_set = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20))

    return render(request, "hello.html", {"name": "Indra", "products": list(query_set)})
