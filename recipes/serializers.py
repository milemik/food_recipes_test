from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from accounts.models import Account
from recipes.models import Ingredients, Recipes, Rating
from recipes.utils import is_recipe_owner, get_average_rating, check_if_user_rated_ones


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ("first_name", "last_name")


class IngredientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredients
        fields = ("name", )


class CreateRecipesSerializer(serializers.ModelSerializer):

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Recipes
        fields = ("author", "name", "recipe_text", "ingredients")


class RecipesSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    average_rating = serializers.SerializerMethodField()
    ingredients = IngredientsSerializer(many=True)

    class Meta:
        model = Recipes
        fields = ("author", "name", "recipe_text", "ingredients", "average_rating")

    def get_average_rating(self, obj):
        return get_average_rating(obj.pk)


class RatingSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Rating
        fields = ("user", "recipe", "rate")

    def create(self, validated_data):
        if is_recipe_owner(validated_data):
            raise ValidationError("Can't rate your recipe!")
        if check_if_user_rated_ones(validated_data):
            raise ValidationError("You already voted once!")
        return Rating.objects.create(**validated_data)
