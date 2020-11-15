from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from accounts.models import Account
from accounts.serializers import CreateAccountSerializer, AccountSerializer


class CreateAccountView(generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = Account.objects.all()
    serializer_class = CreateAccountSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AccountInfo(generics.GenericAPIView, mixins.RetrieveModelMixin):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
