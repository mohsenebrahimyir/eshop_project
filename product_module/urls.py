# product_madule/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name="product-list"),
    path('<str:slug>', views.product_detail, name="product-detail")
]
