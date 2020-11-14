from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from recipes.models import Ingredients, Recipes, Rating
from recipes.utils import is_recipe_owner


class IngredientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredients
        fileds = ("name", )


class CreateRecipesSerializer(serializers.ModelSerializer):

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Recipes
        fields = ("author", "name", "recipe_text",)


class RecipesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipes
        fields = ("author", "name", "recipe_text", "ingredients")


class RatingSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Rating
        fields = ("user", "recipe", "rate")

    def create(self, validated_data):
        if is_recipe_owner(validated_data):
            raise ValidationError("Can't rate your recipe!")
        return Rating.objects.create(**validated_data)
