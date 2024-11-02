import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.card_page import CardPage
from pages.authorization_page import AuthorizationPage

from utils import attach

DEFAULT_BROWSER_VERSION = '100.0'


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != '' else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.driver = driver

    browser.config.driver_name = "chrome"
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture(scope='function')
def main_page():
    main_page = MainPage()
    return main_page


@pytest.fixture(scope='function')
def search_page():
    search_page = SearchPage()
    return search_page


@pytest.fixture(scope='function')
def card_page():
    card_page = CardPage()
    return card_page


@pytest.fixture(scope='function')
def authorization_page():
    authorization_page = AuthorizationPage()
    return authorization_page


@pytest.fixture(scope='session', autouse=True)
def open_browser():
    browser.open('https://www.perekrestok.ru')
