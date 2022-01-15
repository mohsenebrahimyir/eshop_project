# product_module/views.py
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Avg
from django.views.generic import TemplateView


class ProductListView(TemplateView):
    template_name = 'product_module/product_list.html'
    
    def get_context_data(self, **kwargs):
        products = Product.objects.all().order_by('-price')[:5]
        context = super(ProductListView, self).get_context_data()
        context['products'] = products
        
        return context

# def product_list(request):
#     products = Product.objects.all().order_by('-price')[:5]
#     return render(request, 'product_module/product_list.html', {
#         'products': products,
#     })


class ProductDetailView(TemplateView):
    template_name = 'product_module/product_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        slug = kwargs['slug']
        product = get_object_or_404(Product, slug=slug)
        context['product'] = product

# def product_detail(request, slug):
#     product = get_object_or_404(Product, slug=slug)
#     return render(request, 'product_module/product_detail.html', {
#         'product': product
#     })
