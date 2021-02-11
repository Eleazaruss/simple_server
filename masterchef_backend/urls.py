from django.urls import path
from masterchef_backend.views import recipes_response, new, edit, delete

urlpatterns = [
    path('recipes/', recipes_response),
    path('new/', new),
    path('edit/<int:id>', edit),
    path('delete/<int:id>', delete)
]
