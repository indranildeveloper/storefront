from django.core.mail import mail_admins, send_mail
from django.core.mail.message import BadHeaderError
from django.db import transaction
from django.shortcuts import render

from store.models import Order, OrderItem

# Create your views here.


def say_hello(request):
    try:
        # send_mail("subject", "message", "info@storefront.com", ["bob@storefront.com"])
        mail_admins(
            "subject",
            "message",
            html_message="message",
        )
    except BadHeaderError:
        pass
    with transaction.atomic():
        order = Order()
        order.customer_id = 1
        order.save()

        item = OrderItem()
        item.order = order
        item.product_id = 1
        item.quantity = 1
        # pyrefly: ignore [bad-assignment]
        item.unit_price = 10
        item.save()

    return render(
        request,
        "hello.html",
        {"name": "Indra"},
    )
