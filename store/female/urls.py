from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', views.WomansView.as_view(), name='womens'),
    path('<slug:slug>', cache_page(60 * 2)(views.ProductDetailViewWomans.as_view()), name='womans_product'),
]