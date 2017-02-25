def test_delete_first_group(app):  # parametr "app" zapuskaet fixturu
    app.session.login(username="admin", password="secret")
    # sozdaem obekt tipa Group i peredaem perametri v ego konstruktor
    app.group.delete_first_group()
    app.session.logout()
