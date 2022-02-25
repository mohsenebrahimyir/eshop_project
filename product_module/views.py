# product_module/views.py
from django.shortcuts import redirect
from django.views import View
from .models import Product
from django.views.generic import ListView, DetailView


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 6

class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        request = self.request
        favorite_product_id = request.session.get("product_favorite")
        context["is_favorite"] = favorite_product_id == str(loaded_product.id)
        return context

class AddProductFavorite(View):
    def post(self, request):
        product_id = request.POST["product_id"]
        product = Product.objects.get(pk=product_id)
        request.session["product_favorite"] = product_id
        return redirect(product.get_absolute_url())
