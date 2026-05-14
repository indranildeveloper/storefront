from django.shortcuts import render

from store.models import Order

# Create your views here.


def say_hello(request):
    # select_related (1)
    # prefetch_related (n)
    # query_set = Product.objects.select_related("collection").all()
    # query_set = (
    #     Product.objects.prefetch_related("promotions")
    #     .select_related("collection")
    #     .all()
    # )

    query_set = (
        Order.objects.select_related("customer")
        .prefetch_related("orderitem_set__product")
        .order_by("-placed_at")[:5]
    )

    return render(request, "hello.html", {"name": "Indra", "orders": list(query_set)})
