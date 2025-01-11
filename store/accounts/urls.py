from django.urls import path
from .views import authView, loginView
from main.views import main_view
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', main_view, name='main_view'),
    path('login', loginView, name='loginView'),
    path('signup', authView, name='authView'),
    
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='reset_password.html'), name='reset'),
    path('password-reset-done/', auth_view.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]