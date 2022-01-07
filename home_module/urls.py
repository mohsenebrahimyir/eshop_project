from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('', views.index_page, name='home_page'),
    # path('site-header', views.site_header_component, name="site_header_component"),
    # path('site-footer', views.site_footer_component, name="site_footer_component"),
]
