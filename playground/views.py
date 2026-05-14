from django.shortcuts import render
from django.db.models import Value, F, Func, Count
from django.db.models.functions import Concat
from store.models import Product, Customer

# Create your views here.


def say_hello(request):
    # query_set = Customer.objects.annotate(
    #     full_name=Func(F("first_name"), Value(" "), F("last_name"), function="CONCAT")
    # )
    query_set = Customer.objects.annotate(orders_count=Count("order"))

    return render(request, "hello.html", {"name": "Indra", "result": list(query_set)})
