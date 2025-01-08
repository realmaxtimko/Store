from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls 

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('mans/', include('male.urls')),
    path('womans/', include('female.urls')),
    path('boys/', include('boys.urls')),
    path('girls/', include('girls.urls')),
    path('cart/', include('cart.urls')),
    path('', include('main.urls')),
     path('api-auth/', include('rest_framework.urls')),

] + debug_toolbar_urls() + static(settings.STATIC_URL)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)