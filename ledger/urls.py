from django.urls import path
from .views import RecipeListView, RecipeDetailView, ImageAddView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/<int:pk>/add_image', ImageAddView.as_view(), name='image_add'), 
    path('recipe/add'), 
]

app_name = "ledger"
