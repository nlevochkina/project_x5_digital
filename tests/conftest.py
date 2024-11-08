import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.page import Page

from utils import attach

DEFAULT_BROWSER_VERSION = '100.0'


def pytest_addoption(parser):
    parser.addoption(
        '--run_local',
        action='store',
        default='false'
    )
    parser.addoption(
        '--browser_version',
        default=DEFAULT_BROWSER_VERSION
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version') or DEFAULT_BROWSER_VERSION
    is_run_locally = request.config.getoption('--run_local') == 'true'
    options = Options()

    if is_run_locally:
        driver = webdriver.Chrome(options=options)
    else:
        options.set_capability('browserName', 'chrome')
        options.set_capability('browserVersion', browser_version)
        options.page_load_strategy = 'eager'
        options.set_capability('selenoid:options', {
            'enableVNC': True,
            'enableVideo': True
        })

        browser.config.driver_name = 'chrome'

        selenoid_login = os.getenv('SELENOID_LOGIN')
        selenoid_password = os.getenv('SELENOID_PASSWORD')
        driver = webdriver.Remote(
            command_executor=f'https://{selenoid_login}:{selenoid_password}@selenoid.autotests.cloud/wd/hub',
            options=options
        )

    browser.config.driver = driver
    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture(scope='function')
def page():
    page = Page()
    return page


@pytest.fixture(scope='function')
def open_browser(setup_browser):
    browser.config.timeout = 15000
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.open('https://www.perekrestok.ru/')
