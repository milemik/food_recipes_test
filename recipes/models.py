from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from accounts.models import Account


class Ingredients(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Recipes(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    recipe_text = models.TextField(null=False, blank=False)
    ingredients = models.ManyToManyField(Ingredients)

    def __str__(self):
        return self.name


class Rating(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(default=5, validators=(MinValueValidator(1), MaxValueValidator(5)))

    def __str__(self):
        return f"{self.recipe}, {self.rating}"
