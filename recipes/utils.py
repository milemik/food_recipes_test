from django.db.models import Avg

from recipes.models import Rating


def is_recipe_owner(data):
    """
    Check if current user is recipe owner
    NOTE: Owner of recipe can't rate his recipe.
    :param data:
    :return:
    """
    recipe = data.get("recipe")
    if recipe.author == data.get("user"):
        return True
    return False


def get_average_rating(pk):
    """
    Get average rating for recipe
    :param pk:
    :return:
    """
    return Rating.objects.filter(recipe=pk).aggregate(Avg("rate"))['rate__avg']
