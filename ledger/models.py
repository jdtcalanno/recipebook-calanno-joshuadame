from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)
    
    def get_absolute_url(self):
        return reverse('ledger:recipeList', args=[str(self.pk)])


class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE, 
        related_name='recipes')
    created_on = models.DateTimeField(
        auto_now_add=True, 
        null=True)
    updated_on = models.DateTimeField(
        auto_now=True, 
        null=True)

    def __str__(self):
        return 'Recipe: {}'.format(self.name)
    
    def get_absolute_url(self):
        return reverse('ledger:recipe_list', args=[str(self.pk)])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=10)
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE, 
        related_name='recipes')
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE, 
        related_name='recipe_ingredients')


class RecipeImage(models.Model):
    image = models.ImageField(upload_to='images/', null=False)
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='images')
