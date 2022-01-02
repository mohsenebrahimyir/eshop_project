# product_module/admin.py
from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }


admin.site.register(models.Product, ProductAdmin)
