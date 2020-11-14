from django.urls import path

from recipes.views import IngredientsView

urlpatterns = [
    path("ingredients/", IngredientsView.as_view(), name="ingredients"),
]
