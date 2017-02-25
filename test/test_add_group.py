import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application() #sozdanie fixture
    request.addfinalizer(fixture.destroy) #ukazanie na to, kak fixture dolzna bit razrusena
    return fixture

def test_add_group(app):  # self - obekt, v kotorom vizivaetsa metod
    app.session.login(username="admin", password="secret")
    # sozdaem obekt tipa Group i peredaem perametri v ego konstruktor
    app.group.create(Group(name="fdgsgh", header="dsfgsdfg", footer="xcbcvx"))
    app.session.logout()

def test_add_empty_group(app):  # self - obekt, v kotorom vizivaetsa metod
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
