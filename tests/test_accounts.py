import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from accounts.models import Account
from tests.factories import AccountFactory


@pytest.mark.django_db
def test_account_create_model():
    acc = Account.objects.create(
        email="testmail@mail.com",
        first_name="Somename",
        last_name="Somelastname",
    )

    acc.set_password("testpass")
    assert Account.objects.all().count() == 1


@pytest.mark.django_db
def test_jwt_token():
    password = "djangotest123"
    user = AccountFactory()
    user.set_password(password)
    user.save()

    client = APIClient()

    url = reverse("token_obtain_pair")
    response = client.post(url, {"email": user.email, "password": password})
    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.json()

    token = response.json()['access']
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
    url = reverse("ingredients")
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_account_api():
    data = {
        "email": "mile@gmail.com",
        "first_name": "mile",
        "last_name": "miki",
        "password": "password123"
    }

    url = reverse("create-account")

    client = APIClient()
    response = client.post(url, data=data)

    assert response.status_code == status.HTTP_201_CREATED
    assert Account.objects.filter(email=data['email']).exists()
