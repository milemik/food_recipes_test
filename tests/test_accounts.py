import pytest

from accounts.models import Account


@pytest.mark.django_db
def test_account_create_model():
    acc = Account.objects.create(
        email="testmail@mail.com",
        first_name="Somename",
        last_name="Somelastname",
    )

    acc.set_password("testpass")
    assert Account.objects.all().count() == 1
