import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):  # self - obekt, v kotorom vizivaetsa metod
    app.session.login(username="admin", password="secret")
    app.contact.create(
        Contact(firstname="fsdgsdfg", lastname="xcbsv", address="cfhdsfh", home_phone="fdghsdfh", email_1="sdfgh"))
    app.session.logout()


def test_add_empty_contact(app):  # self - obekt, v kotorom vizivaetsa metod
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", lastname="", address="", home_phone="", email_1=""))
    app.session.logout()
