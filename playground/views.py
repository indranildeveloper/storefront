from django.shortcuts import render

from store.models import Product

# Create your views here.


def say_hello(request):
    query_set = Product.objects.filter(description__isnull=True)

    return render(request, "hello.html", {"name": "Indra", "products": list(query_set)})
