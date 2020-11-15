import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from recipes.models import Ingredients, Recipes, Rating
from tests.factories import AccountFactory, IngredientsFactory, RecipesFactory, RatingFactory


@pytest.fixture
def user_client():
    user = AccountFactory()
    client = APIClient()
    client.force_authenticate(user=user)

    return user, client


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
    user2 = AccountFactory()
    ingredients = IngredientsFactory()
    recipes = RecipesFactory(author=user)
    recipes.ingredients.add(ingredients)

    Rating.objects.create(
        user=user2,
        recipe=recipes,
        rate=3
    )

    assert Rating.objects.all().count() == 1


@pytest.mark.django_db
def test_ingredients_api():
    url = reverse("ingredients")
    client = APIClient()

    response = client.get(url)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_create_recipes(user_client):
    user, client = user_client
    url = reverse("create-recipes")

    response = client.post(url, {"name": "TestName", "recipe_text": "Some recipe text here"})

    assert response.status_code == status.HTTP_201_CREATED
    assert Recipes.objects.filter(author=user).exists()


@pytest.mark.django_db
def test_all_recipes_api(user_client):
    user, client = user_client
    user2 = AccountFactory()
    recipe = RecipesFactory(author=user)
    RatingFactory(recipe=recipe, user=user2, rate=5)
    url = reverse("all-recipes")

    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()[0]['average_rating'] == 5.0


@pytest.mark.django_db
def test_rate_api(user_client):
    user, client = user_client
    user2 = AccountFactory()
    recipe = RecipesFactory(author=user2)
    url = reverse("rate")

    response = client.post(url, {"recipe": recipe.pk, "rate": 4})

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_rate_api(user_client):
    user, client = user_client
    recipe = RecipesFactory(author=user)
    url = reverse("rate")

    response = client.post(url, {"recipe": recipe.pk, "rate": 4})
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_average_rate(user_client):
    user, client = user_client
    recipe = RecipesFactory(author=user)
    user2 = AccountFactory()
    user3 = AccountFactory()
    user4 = AccountFactory()
    user5 = AccountFactory()
    RatingFactory(recipe=recipe, user=user2, rate=3)
    RatingFactory(recipe=recipe, user=user3, rate=5)
    RatingFactory(recipe=recipe, user=user4, rate=4)
    RatingFactory(recipe=recipe, user=user5, rate=2)

    expected_average_rate = round((3+5+4+2)/4, 2)

    url = reverse("all-recipes")

    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()[0]['average_rating'] == expected_average_rate
