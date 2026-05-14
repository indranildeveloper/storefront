from django.shortcuts import render
from django.db.models import Q, F

from store.models import Product

# Create your views here.


def say_hello(request):
    query_set = Product.objects.filter(inventory=F("collection__id"))

    return render(request, "hello.html", {"name": "Indra", "products": list(query_set)})
