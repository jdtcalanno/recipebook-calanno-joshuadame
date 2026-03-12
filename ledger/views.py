from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import RecipeIngredient, Recipe, Ingredient, RecipeImage


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipeList.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipeDetail.html'
    login_url = '../accounts/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredient_list'] = RecipeIngredient.objects.filter(
            recipe=self.object)
        return context

    def recipeList(request):
        recipes = Recipe.objects.all()
        ctx = {
            'recipes': recipes
        }
        return render(
            request, 
            "ledger/recipeList.html", 
            ctx)

    def recipeDetail(request):
        ingredients = Ingredient.objects.filter(
            recipe__recipe__name="{{ingredient.recipe.name}}")
        ctx = {
            'ingredients': ingredients
        }
        return render(
            request, 
            "ledger/recipeDetail.html", 
            ctx)


class ImageAddView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/imageAdd.html'
    login_url = '.../accounts/login/'

    def get(self, request, *args, **kwargs):
        recipe = self.get_object()
        return render(request, self.template_name, {'recipe': recipe, 'next': request.GET.get('next')})

    def post(self, request, *args, **kwargs):
        recipe = self.get_object()
        image_file = request.FILES.get("image")
        description = request.POST.get("description", "")

        if image_file:
            RecipeImage.objects.create(
                recipe=recipe,
                image=image_file,
                description=description, 
            )

        return redirect(request.POST.get('next'))
