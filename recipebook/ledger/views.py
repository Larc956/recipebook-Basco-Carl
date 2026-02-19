from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

def index(request):
    return HttpResponse('Recipe Book')
        
def recipe_list(request):
    ctx = {
        "recipes": Recipe.objects.all()
    }
    return render(request, "ledger/recipe_list.html", ctx)

def recipe_detail(request, recipe_id):
    ctx = {
        "recipe": Recipe.objects.get(id=recipe_id)
    }
    return render(request, "ledger/recipe_detail.html", ctx)