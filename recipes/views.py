from django.db.models import F, Count
from rest_framework import generics, mixins, filters
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
    queryset = Recipes.objects.select_related("author").prefetch_related("ingredients").all()
    serializer_class = CreateRecipesSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AllRecipesView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Recipes.objects.prefetch_related("ingredients").all()
    serializer_class = RecipesSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name", "recipe_text", "ingredients__name",)

    def get_queryset(self):
        queryset = Recipes.objects.prefetch_related("ingredients").all()

        max_ingredients_num = self.request.query_params.get("max_ing_num", None)
        if max_ingredients_num:
            queryset = queryset.annotate(total=Count("ingredients")).filter(total__lte=int(max_ingredients_num))
        min_ingredients_num = self.request.query_params.get("min_ing_num", None)
        if min_ingredients_num:
            queryset = queryset.annotate(total=Count("ingredients")).filter(total__gte=int(min_ingredients_num))
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RateView(generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = Rating.objects.select_related("user").all()
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, requests, *args, **kwargs):
        return self.create(requests, *args, **kwargs)
