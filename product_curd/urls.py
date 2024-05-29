from django.urls import path

from product_curd.views import ProductCurd

urlpatterns = [
    path('product/getAll/', ProductCurd.as_view(),name="get all product"),
    path('product/<product_id>/', ProductCurd.as_view(),name="update and get product"),
]
