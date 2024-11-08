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
        '--browser_version',
        default=DEFAULT_BROWSER_VERSION
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope="function", autouse=True)
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != '' else DEFAULT_BROWSER_VERSION
    options = Options()
    is_run_locally = request.config.getoption('--run_local')
    # is_run_locally = request.config.getoption('--run_locally')

    if is_run_locally:
        driver = webdriver.Chrome()
    else:
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        options.capabilities.update(selenoid_capabilities)

        browser.config.driver_name = "chrome"

        selenoid_login = os.getenv('LOGIN')
        selenoid_password = os.getenv('PASSWORD')
        driver = webdriver.Remote(
            command_executor=f"https://{selenoid_login}:{selenoid_password}@selenoid.autotests.cloud/wd/hub",
            options=options
        )
        browser.config.driver = driver

    yield

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
    browser.config.timeout = 12000
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.open('https://www.perekrestok.ru')
