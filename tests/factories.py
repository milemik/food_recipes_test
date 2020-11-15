import factory
from factory.django import DjangoModelFactory

from accounts.models import Account
from recipes.models import Ingredients, Recipes, Rating


class AccountFactory(DjangoModelFactory):
    email = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")

    class Meta:
        model = Account


class IngredientsFactory(DjangoModelFactory):
    name = factory.Faker("name")

    class Meta:
        model = Ingredients


class RecipesFactory(DjangoModelFactory):
    author = factory.SubFactory(AccountFactory)
    name = factory.Faker("name")
    recipe_text = factory.Faker("text")

    class Meta:
        model = Recipes


class RatingFactory(DjangoModelFactory):
    user = factory.SubFactory(AccountFactory)
    recipe = factory.SubFactory(RecipesFactory)
    rate = 3

    class Meta:
        model = Rating
