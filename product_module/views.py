# product_module/views.py
from .models import Product
from django.views.generic import ListView, DetailView


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    
    def get_queryset(self):
        base_query = super(ProductListView, self).get_queryset()
        data = base_query.filter(is_active=True)
        
        return data


class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product
