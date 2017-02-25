import pytest

from fixture.application import Application


@pytest.fixture(scope="session")#brauzer zapuskaetsa 1 raz
def app(request):
    fixture = Application()  # sozdanie fixture
    request.addfinalizer(fixture.destroy)  # ukazanie na to, kak fixture dolzna bit razrusena
    return fixture
