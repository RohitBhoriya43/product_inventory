from django.contrib import admin

from product_curd.models import Products

# Register your models here.

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id","name","category","price")
