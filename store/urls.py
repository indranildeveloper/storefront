from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.product_list, name="products-list"),
    path("products/<int:product_id>/", views.product_detail, name="product-detail"),
    path(
        "collection/<int:pk>/",
        views.collection_detail,
        name="collection-detail",
    ),
]
