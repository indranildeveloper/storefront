from django.shortcuts import render

from .tasks import notify_customers


# Create your views here.
def say_hello(request):
    # pyrefly: ignore [missing-attribute]
    notify_customers.delay("Hello")
    return render(
        request,
        "hello.html",
        {"name": "Indra"},
    )
