from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    
]
