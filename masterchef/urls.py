from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('masterchef/', include('masterchef_backend.urls')) #wczytuje wszystkie urle dla aplikacji masterchef_backend
]
