from django.contrib import admin

from recipes.models import Ingredients, Rating, Recipes


@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    pass


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    pass
