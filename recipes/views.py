from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from recipes.models import Ingredients
from recipes.serializers import IngredientsSerializer


class IngredientsView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
