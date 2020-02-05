# Generated by Selenium IDE

import pytest
from group import group
from application import application


@pytest.fixture
def app(request):
    fixture = application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(group(name="test-1", header="1", footer="2"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(group(name="", header="", footer=""))
    app.logout()
