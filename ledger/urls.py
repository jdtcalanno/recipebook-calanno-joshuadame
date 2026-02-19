from django.urls import path
from .views import RecipeListView, RecipeDetailView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name = 'recipeList'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name = 'recipeDetail'),
]

app_name = "ledger"