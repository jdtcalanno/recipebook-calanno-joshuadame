from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)
    
    def get_absolute_url(self):
        return reverse('myapp:recipeList', args=[str(self.pk)])

class Recipe(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Recipe: {}'.format(self.name)
    
    def get_absolute_url(self):
        return reverse('myapp:recipeList', args=[str(self.pk)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=10)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )