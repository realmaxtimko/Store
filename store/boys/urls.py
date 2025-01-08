from django.urls import path
from . import views


urlpatterns = [
    path('', views.BoysView.as_view(), name='boys'),
    path('<slug:slug>', views.ProductDetailViewBoys.as_view(), name='boys_product'),
]