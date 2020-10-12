from ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--url', default='https://target.my.com/')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--user', default='anonym.213555@mail.ru')
    parser.addoption('--password', default='Lbvfcbr1!')
    parser.addoption('--selenoid', default=False)


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    user_email = request.config.getoption('--user')
    user_password = request.config.getoption('--password')
    selenoid = request.config.getoption('--selenoid')

    return {'browser': browser, 'version': version, 'url': url, 'email': user_email,
            'password': user_password, 'selenoid': selenoid, 'download_dir': '/tmp'}
