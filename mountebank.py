import requests
import json

MOUNTEBANK_HOST = 'http://localhost'
MOUNTEBANK_URL = MOUNTEBANK_HOST + ':2525'
IMPOSTERS_URL = MOUNTEBANK_URL + '/imposters'


def create_imposter(definition):
    if isinstance(definition, dict):
        return requests.post(IMPOSTERS_URL, data=definition)
    else:
        return requests.post(IMPOSTERS_URL, data=definition)


def delete_all_imposters():
    return requests.delete(IMPOSTERS_URL)


def delete_imposter(port):
    return requests.delete("{}/imposters/{}".format(MOUNTEBANK_URL, port))


def get_all_imposters():
    return requests.get(IMPOSTERS_URL)


def get_imposter(port):
    print "{}/imposters/{}".format(MOUNTEBANK_URL, port)
    return requests.get("{}/imposters/{}".format(MOUNTEBANK_URL, port))


class MountebankException(Exception):
    pass


class Microservice(object):

    def __init__(self, definition):
        resp = create_imposter(definition)
        if resp.status_code != 201:
            raise MountebankException("{}: {}".format(resp.status_code, resp.text))
        self.port = resp.json()['port']

    def get_url(self, *endpoint):
        return "{}:{}{}".format(MOUNTEBANK_HOST, self.port, "".join('/' + name for name in endpoint))

    def get_self(self):
        return get_imposter(self.port)

    def destroy(self):
        return delete_imposter(self.port)

import pytest
@pytest.fixture(scope='session')
def sales_mock(request):
    definition = request.config.getOption('definition')
    m = Microservice(definition)
    request.addfinalizers(m.destroy)
    return m

@pytest.fixture
def driver(request):
    browser = request.config.getOption('browser')
    url = request.config.getOption('remoteHost')
    d = Remote(url, browser)
    request.addfinalizer(d.quit)
    return d

