import pytest

from recipes.models import Ingredients, Recipes, Rating
from tests.factories import AccountFactory, IngredientsFactory, RecipesFactory


@pytest.mark.django_db
def test_create_ingredients():
    Ingredients.objects.create(
        name="Sugar"
    )

    assert Ingredients.objects.filter(name="Sugar").exists()


@pytest.mark.django_db
def test_create_recipe():
    user = AccountFactory()
    ingredients = IngredientsFactory()
    rec = Recipes.objects.create(
        author=user,
        name="TryMe",
        recipe_text="Some recipe here",
    )
    rec.ingredients.add(ingredients)
    assert Recipes.objects.filter(author=user).exists()
    assert ingredients in Recipes.objects.get(author=user).ingredients.all()


@pytest.mark.django_db
def test_create_rating():
    user = AccountFactory()
    ingredients = IngredientsFactory()
    recipes = RecipesFactory(author=user)
    recipes.ingredients.add(ingredients)

    Rating.objects.create(
        recipe=recipes,
        rate=3
    )

    assert Rating.objects.all().count() == 1
