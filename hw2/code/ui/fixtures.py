import pytest
import json
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.segment_page import SegmentPage
import datetime
import os



class UnsupportedBrowserException(Exception):
    pass


@pytest.fixture(scope='function')
def driver(config):
    browser = config['browser']
    version = config['version']
    url = config['url']
    selenoid = config['selenoid']
    download_dir = config['download_dir']

    if browser == 'chrome':
        options = ChromeOptions()
        if selenoid is False:
            # options.add_argument("--window-size=800,600")
            prefs = {"download.default_directory": download_dir}
            options.add_experimental_option('prefs', prefs)
            manager = ChromeDriverManager(version=version)
            driver = webdriver.Chrome(executable_path=manager.install(),
                                      options=options,
                                      desired_capabilities={'acceptInsecureCerts': True}
                                       )
        else:
            driver = webdriver.Remote(command_executor='selenoid',
                                      options=options,
                                      desired_capabilities={'acceptInsecureCerts': True,
                                                            'browserName': 'chrome',
                                                            'version': '80.0'
                                                            }
                                      )
    else:
        raise UnsupportedBrowserException(f'Unsupported browser: "{browser}"')

    driver.get(url)
    driver.maximize_window()
    yield driver

    driver.quit()


@pytest.fixture
def main_page(driver, config):
    return MainPage(driver=driver, config=config)


@pytest.fixture
def base_page(driver, config):
    return BasePage(driver=driver, config=config)


@pytest.fixture
def segment_page(driver, config):
    return SegmentPage(driver=driver, config=config)


@pytest.fixture
def auth(driver, config):

    page_object = BasePage(driver, config)
    login = config['email']
    paswd = config['password']
    locator = basic_locators.BasePageLocators()
    page_object.click(locator.AUTH_BUTTON)
    page_object.find(locator.EMAIL).send_keys(login)
    page_object.find(locator.PASSWORD).send_keys(paswd)
    page_object.click(locator.ACCEPT)

    return MainPage(driver, config)


@pytest.fixture(scope='function')
def incorrect_input(driver, config):

    page_object = BasePage(driver, config)
    login = 'Incorrect_user_email@mail.ru'
    paswd = 'Incorrect_user_password'
    config['fake_email'] = login
    locator = basic_locators.BasePageLocators()
    page_object.click(locator.AUTH_BUTTON)
    page_object.find(locator.EMAIL).send_keys(login)
    page_object.find(locator.PASSWORD).send_keys(paswd)
    page_object.click(locator.ACCEPT)

    return MainPage(driver, config)


@pytest.fixture(scope='function')
def generated_data():
    """
    Фикстура, возвращающая датасет для создания компании по шаблону

    :return: (path, name)
    """
    dirname = os.path.dirname(__file__)
    PATH_TO_FILE = os.path.join(dirname, 'test_company.json')
    new_name = 'New company ' + str(datetime.datetime.now())
    with open(PATH_TO_FILE, 'r') as f:
        file = json.load(f)
        file['name'] = new_name
    with open('temp_file.json', 'w') as f:
        json.dump(file, f)
    return os.path.abspath('temp_file.json'), "Копия " + new_name