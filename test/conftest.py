# -*- coding: utf-8 -*-
import json
import os.path
import pytest
from fixture.application import Application

fixture = None
configuration = None

@pytest.fixture
def app(request):
    global fixture
    global configuration
    browser = request.config.getoption('--browser')
    # __file__ wskazuje lokalizację bieżącego pliku, ale może być absolutna lub względna
    if configuration is None:
        config_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), request.config.getoption('--configuration'))
        with open(config_file) as config:
            configuration = json.load(config)
    try:
        if fixture is None or not fixture.is_valid():
            fixture = Application(browser=browser, base_url=configuration['baseUrl'])
        fixture.session.ensure_login(username=configuration['username'], password=configuration['password'])
    except ValueError:
        print('Logowanie nie powiodło się.\n Logging in error.')
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--configuration', action='store', default='configuration.json')


