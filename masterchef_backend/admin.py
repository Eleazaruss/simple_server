from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name", "category"]
    list_filter = ("category", "isFavorite")
    search_fields = ("name",)