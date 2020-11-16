from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from accounts.views import CreateAccountView, AccountInfo

urlpatterns = [
    path('create/', CreateAccountView.as_view(), name="create-account"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<int:pk>/', AccountInfo.as_view(), name="account-info"),
]
