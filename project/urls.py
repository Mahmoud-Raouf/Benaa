from django.contrib import admin
from django.urls import path ,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('request/', include('request.urls' , namespace='request')),
    path('users/', include('accounts.urls' , namespace='accounts')),
    path('orders/', include('orders.urls' , namespace='orders')),
    path('dashboard/', include('dashboard.urls' , namespace='dashboard')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)