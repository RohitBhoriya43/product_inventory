from django.urls import path

from product_curd.views import ProductCurd

urlpatterns = [
    path('product/getAll/', ProductCurd.as_view(),name="get all product"),
    path('product/<product_id>/update/', ProductCurd.as_view(),name="update product"),
    path('product/<product_id>/delete/', ProductCurd.as_view(),name="delete product"),
    path('product/<product_id>/get/', ProductCurd.as_view(),name="get product"),
]
