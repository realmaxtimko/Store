from django.urls import path
from .views import authView, loginView
from main.views import main_view


urlpatterns = [
    path('', main_view, name='main_view'),
    path('account/login', loginView, name='loginView'),
    path('account/signup', authView, name='authView')
]