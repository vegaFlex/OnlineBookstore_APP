
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookstore.urls')),  # Това добавя маршрута за началната страница
    path('bookstore/', include('bookstore.urls')),  # Това е маршрута за страниците на приложението
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
