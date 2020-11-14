from django.urls import path

from recipes.views import IngredientsView, CreateRecipesView, AllRecipesView, RateView

urlpatterns = [
    path("ingredients/", IngredientsView.as_view(), name="ingredients"),
    path("recipes/", AllRecipesView.as_view(), name="all-recipes"),
    path("recipes/create/", CreateRecipesView.as_view(), name="create-recipes"),
    path("recipes/rate/", RateView.as_view(), name="rate")
]
