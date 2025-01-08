from django.urls import path
from . import views
from accounts.views import logoutView, loginView, authView
from cart.views import cartView, RemoveFromCart
from .views import ObjectAPIView
from wishlist.views import add_to_wishlist


urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('signup/', authView, name='authView'),
    path('login/', loginView, name='loginView'),
    path('reference/', views.reference_view, name='reference'),
    path('search/', views.search_view, name='search'),
    path('logout/', logoutView, name='logoutView'),
    path('cart/', cartView, name='cart'),
    path('cart/remove/<str:app_label>/<str:model_name>/<int:object_id>/', RemoveFromCart, name='remove'),
    path('api/v1/womas', ObjectAPIView.as_view()),
    path('add/<str:app_label>/<str:model_name>/', add_to_wishlist, name='like'),
]