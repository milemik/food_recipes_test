from accounts.utils import check_email


def test_check_mail():
    mail = "mileta99@gmail.com"
    assert check_email(mail)

    fake_mail = "test@test.com"
    assert not check_email(fake_mail)
