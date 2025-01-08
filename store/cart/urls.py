from django.urls import path
from . import views

urlpatterns = [
     path('add/<str:app_label>/<str:model_name>/<int:object_id>/', views.add_to_cart, name='add_to_cart'),
]
