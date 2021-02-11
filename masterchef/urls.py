from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('masterchef/', include('masterchef_backend.urls')) #wczytuje wszystkie urle dla aplikacji masterchef_backend
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)