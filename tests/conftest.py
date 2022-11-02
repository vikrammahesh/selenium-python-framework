import os
import shutil

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from Utilities import logger_utils
from Utilities.action_utils import ActionUtils
from Utilities.base_test import BaseTest


driver = None
log = logger_utils.get_logger()


@pytest.fixture(scope="class")
def actions_utils(request):
    request.cls.action_utils = ActionUtils(driver)


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser = request.config.getoption('--browser')
    log.info('Setting driver for ' + browser)
    if browser == 'chrome':
        # service_obj = Service("/home/maheshvikram/Documents/drivers/chromedriver")
        # driver = webdriver.Chrome(service=service_obj)
        try:
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        except Exception as e:
            log.error(e)
    elif browser == "firefox":
        webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        # options = webdriver.FirefoxOptions()
        # options.add_argument("--headless")
        # options.add_argument("--disable-gpu")
        # driver_path = FirefoxService(r"/home/maheshvikram/Documents/drivers/geckodriver")
        # driver = webdriver.Firefox(service=driver_path, options=options)

    else:
        raise Exception('No driver initiated')
    driver.implicitly_wait(4)
    request.cls.driver = driver
    yield
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        '--browser', action='store', default='chrome', help='Browser to execute tests'
    )


@pytest.fixture(scope="class")
def get_browser(request):
    return request.config.getoption('--browser')


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if (report.when == 'call' or report.when == "setup") and (report.failed or report.skipped):
        try:
            allure.attach(driver.get_screenshot_as_png(), name='Screnshot', attachment_type=AttachmentType.PNG)
        except Exception as e:
            log.error('Fail to take screenshot: ' .format(e))


@pytest.hookimpl(tryfirst=True)
def pytest_configure():
    path = BaseTest.ROOT_PATH + '/allure-results'
    try:
        if os.path.exists(path):
            shutil.rmtree(path)
        os.makedirs(path)
        with open(os.path.join(path, 'environment.properties'), 'w') as temp_file:
            temp_file.write("Browser=" + os.environ['browser'] + '\n' + "Environment=" + os.environ['testenv'] + '\n' + "Url=" + os.environ['url'])
    except OSError as e:
        log.error("Error: %s - %s." % (e.filename, e.strerror))
