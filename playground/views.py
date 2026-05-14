from django.shortcuts import render
from django.db.models import Value, F
from store.models import Product, Customer

# Create your views here.


def say_hello(request):
    query_set = Customer.objects.annotate(new_id=F("id"))

    return render(request, "hello.html", {"name": "Indra", "result": list(query_set)})
