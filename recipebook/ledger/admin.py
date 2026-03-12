from django.contrib import admin
from .models import Recipe, RecipeIngredient, RecipeImage

class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient

class RecipeImageInLine(admin.TabularInline):
    model = RecipeImage

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [
        RecipeIngredientInLine,
        RecipeImageInLine,
    ]
    search_fields = ("name",)
    list_display = ("name",)

    fieldsets = [("Details", {"fields": ["name"]})]

admin.site.register(Recipe, RecipeAdmin)