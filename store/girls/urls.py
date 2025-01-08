from django.urls import path
from . import views


urlpatterns = [
    path('', views.GirlsView.as_view(), name='girls'),
    path('<slug:slug>', views.ProductDetailViewGirls.as_view(), name='girls_product')
]