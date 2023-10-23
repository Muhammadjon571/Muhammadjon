from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name="index_url"),
    path('create-product/', create_product_view, name="create_product_url"),
    path('search-product/', search_product_view, name="search_product_url"),
    path('update-product/<int:pk>/', update_product_view, name="update_product_url"),
    path('delete-product/<int:pk>/', delete_product_view, name="delete_product_url")
]
