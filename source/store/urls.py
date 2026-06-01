from store.views import (products, add_product, categories, add_category,
                         product_detail, product_edit, category_detail, category_edit)
from django.urls import path

urlpatterns = [
    path("", products, name="products"),
    path("products/", products, name="products"),
    path("products/add/", add_product, name="add_product"),
    path("products/<int:pk>/", product_detail, name="product_detail"),
    path("products/<int:pk>/edit/", product_edit, name="product_edit"),
    path("categories/", categories, name="categories"),
    path("categories/add/", add_category, name="add_category"),
    path("categories/<int:pk>/", category_detail, name="category_detail"),
    path("categories/<int:pk>/edit", category_edit, name="category_edit"),
]