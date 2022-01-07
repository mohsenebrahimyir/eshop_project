# eshop_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home_module.urls')),
    path('products/', include('product_module.urls')),
    path('contact-us/', include('contact_module.urls')),
    path('admin/', admin.site.urls),
]

admin.site.site_header = 'مدیریت فروشگاه اینترنتی'
admin.site.site_title = 'مدیریت فروشگاه اینترنتی'
