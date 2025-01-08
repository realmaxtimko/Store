from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', views.MensView.as_view(), name='mans'),
    path('<slug:slug>', cache_page(60 * 2)(views.ProductDetailViewMens.as_view()), name='mans_product')
]