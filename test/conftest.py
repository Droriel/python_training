# -*- coding: utf-8 -*-
import json
import os.path
import pytest
from fixture.application import Application
import importlib
import jsonpickle

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


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testData = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testData, ids=[str(x) for x in testData])
        elif fixture.startswith("json_"):
            testData = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testData, ids=[str(x) for x in testData])


def load_from_module(module):
    return importlib.import_module('data.%s' % module).testData


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data/%s.json" %file)) as f:
        return jsonpickle.decode(f.read())



