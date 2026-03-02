from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline]
    list_display = ('name', 'author', 'created_on', 'updated_on', )
    list_filter = ('author', )
    search_fields = ('name', )


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ('name', )


class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    search_fields = ('quantity', )
    list_display = ('quantity', 'recipe', 'ingredient', )
    list_filter = ('quantity', )
    fieldsets = [
        ('Details', {
            'fields': [
                ('quantity'), 'recipe', 'ingredient'
            ]
        }),
    ]


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
