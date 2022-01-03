# product_module/views.py
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Avg


def product_list(request):
    products = Product.objects.all().order_by('title')
    number_of_products = products.count()
    return render(request, 'product_module/product_list.html', {
        'products': products,
        'totale_number_of_products': number_of_products
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_module/product_detail.html', {
        'product': product
    })
