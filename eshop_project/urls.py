# eshop_project/urls.py
from pydoc import doc
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('home_module.urls')),
    path('products/', include('product_module.urls')),
    path('contact-us/', include('contact_module.urls')),
    path('admin/', admin.site.urls),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.site_header = 'مدیریت فروشگاه اینترنتی'
admin.site.site_title = 'مدیریت فروشگاه اینترنتی'
