from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from recipes.models import Ingredients, Recipes, Rating
from recipes.serializers import IngredientsSerializer, CreateRecipesSerializer, RecipesSerializer, RatingSerializer


class IngredientsView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CreateRecipesView(generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = Recipes.objects.all()
    serializer_class = CreateRecipesSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AllRecipesView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RateView(generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, requests, *args, **kwargs):
        return self.create(requests, *args, **kwargs)
