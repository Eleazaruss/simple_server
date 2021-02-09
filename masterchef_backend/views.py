from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

def test_response(request):
    allRecipe = Recipe.objects.all()
    return render(request, 'recipes.html', {'recipes': allRecipe})
