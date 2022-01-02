# eshop_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product_module.urls')),
]

admin.site.site_header = 'مدیریت فروشگاه اینترنتی'
admin.site.site_title = 'مدیریت فروشگاه اینترنتی'
