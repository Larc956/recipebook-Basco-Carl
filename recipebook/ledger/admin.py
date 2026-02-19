from django.contrib import admin

from .models import Recipe, Ingredient, RecipeIngredient

class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInLine,]
    search_fields = ('name',)
    list_display = ('name',)

    fieldsets = [
        ('Details', {
            'fields': [
                'name'
            ]
        })
    ]

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    search_fields = ('quantity',)
    list_display = ('quantity', 'ingredient', 'recipe')
    list_filter = ('recipe', 'ingredient')

    fieldsets = [
        ('Details', {
            'fields': [
                ('quantity', 'ingredient'), 'recipe' 
            ]
        })
    ]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)