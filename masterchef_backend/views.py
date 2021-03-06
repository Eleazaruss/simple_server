from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required

def recipes_response(request):
    allRecipe = Recipe.objects.all()
    return render(request, 'recipes.html', {'recipes': allRecipe})

@login_required()
def new(request):
    form = RecipeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(recipes_response)
    return render(request, 'recipe_form.html', {'form': form})

@login_required()
def edit(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    form = RecipeForm(request.POST or None, request.FILES or None, instance=recipe)
    if form.is_valid():
        form.save()
        return redirect(recipes_response)
    return render(request, 'recipe_form.html', {'form': form})

@login_required()
def delete(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    if request.method == "POST":
        recipe.delete()
        return redirect(recipes_response)
    return render(request, 'confirmation.html', {'recipe': recipe})
