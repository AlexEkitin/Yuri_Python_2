from selenium import webdriver

from application import Application
from group import Group

import pytest

@pytest.fixture
def app(request):
    fixture = Application() #sozdanie fixture
    request.addfinalizer(fixture.destroy) #ukazanie na to, kak fixture dolzna bit razrusena
    return fixture

def test_add_group(app):  # self - obekt, v kotorom vizivaetsa metod
    app.login(username="admin", password="secret")
    # sozdaem obekt tipa Group i peredaem perametri v ego konstruktor
    app.create_group(Group(name="fdgsgh", header="dsfgsdfg", footer="xcbcvx"))
    app.logout()

def test_add_empty_group(app):  # self - obekt, v kotorom vizivaetsa metod
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
