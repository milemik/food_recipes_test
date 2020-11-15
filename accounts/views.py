from rest_framework import generics, mixins

from accounts.models import Account
from accounts.serializers import CreateAccountSerializer


class CreateAccountView(generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = Account.objects.all()
    serializer_class = CreateAccountSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
