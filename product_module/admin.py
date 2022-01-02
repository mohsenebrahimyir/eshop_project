# product_module/admin.py
from django.contrib import admin
from . import models


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title']


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }

    list_display = ['title', 'price', 'rating', 'is_active']
    list_filter = ['rating', 'is_active']
    list_editable = ['rating', 'is_active']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory, ProductCategoryAdmin)