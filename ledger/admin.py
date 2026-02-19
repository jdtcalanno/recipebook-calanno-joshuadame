from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    search_fields = ('quantity',)
    list_display = ('quantity','recipe','ingredient')
    list_filter = ('quantity',)
    fieldsets = [
        # fieldsets is a list of tuples where the syntax is:
        # ('label of the field', {'fields': [<list of fields>]})
        ('Details', {
            'fields': [
                # the tuple puts these fields in a single line
                ('quantity'), 'recipe', 'ingredient'
            ]
        }),
    ]

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline]
    list_display = ('name',)

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ('name',)

# registering the model and the admin is what tells
# Django that admin pages must be generated for the models specified
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)