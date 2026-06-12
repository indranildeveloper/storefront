import requests

# from django.core.cache import cache
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView

# from .tasks import notify_customers


# Create your views here.


class HelloView(APIView):
    @method_decorator(cache_page(60 * 5))  # Cache the view for 5 minutes
    def get(self, request):
        response = requests.get("https://httpbin.org/delay/2", timeout=20)
        data = response.text
        return render(
            request,
            "hello.html",
            {"name": data},
        )


# @cache_page(60 * 5)  # Cache the view for 5 minutes
# def say_hello(request):
#     # pyrefly: ignore [missing-attribute]
#     # notify_customers.delay("Hello")

#     response = requests.get("https://httpbin.org/delay/2", timeout=5)
#     data = response.text
#     return render(
#         request,
#         "hello.html",
#         {"name": "Indra"},
#     )
