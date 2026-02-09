from django.urls import path
from .views import index, recipe_list, recipe_one, recipe_two

urlpatterns = [
    path('', index, name="index"),
    path('recipes/list', recipe_list, name='list'),
    path('recipe/1', recipe_one, name='one'),
    path('recipe/2', recipe_two, name='two'),
]

app_name = "ledger"