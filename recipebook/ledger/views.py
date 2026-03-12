from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Recipe, RecipeImage

class RecipeListView(ListView):
    model = Recipe
    template_name = "ledger/recipe_list.html"
    context_object_name = "recipes"

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "ledger/recipe_detail.html"
    context_object_name = "recipe"

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['name']
    template_name = "ledger/recipe_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    fields = ['image', 'description']
    template_name = "ledger/recipe_image_form.html"

    def form_valid(self, form):
        recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        form.instance.recipe = recipe
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ledger:recipe_detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = Recipe.objects.get(pk=self.kwargs['pk'])
        return context