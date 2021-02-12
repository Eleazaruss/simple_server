from django.urls import path
from masterchef_backend.views import recipes_response, new, edit, delete

urlpatterns = [
    path('recipes/', recipes_response, name="all_recipe"),
    path('new/', new, name="new_recipe"),
    path('edit/<int:id>', edit, name="edit_recipe"),
    path('delete/<int:id>', delete, name="delete_recipe")
]
