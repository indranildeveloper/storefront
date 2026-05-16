from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.ProductList.as_view(), name="products-list"),
    path(
        "products/<int:product_id>/",
        views.ProductDetail.as_view(),
        name="product-detail",
    ),
    path("collections/", views.CollectionList.as_view(), name="collection-list"),
    path(
        "collections/<int:pk>/",
        views.collection_detail,
        name="collection-detail",
    ),
]
