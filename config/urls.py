from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from app.views import pay

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pay/', pay, name="pay"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
