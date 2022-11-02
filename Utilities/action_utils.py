from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

from Utilities import logger_utils


class ActionUtils:

    log = logger_utils.get_logger()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def find_element(self, *element):
        return self.driver.find_element(*element)

    def verify_link_text_presence(self, text):
        self.wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def select_option_by_text(self, text, *web_element):
        self.log.info("# Select an option from dropdown... {}".format(web_element))
        sel = Select(self.find_element(*web_element))
        sel.select_by_visible_text(text)

    def web_driver_wait(self, timeout):
        return WebDriverWait(self.driver, timeout)

    def wait_for_element(self, *web_element, timeout=20):
        self.log.info("Wait for element to appear...{}" .format(web_element))
        self.wait.until(expected_conditions.presence_of_element_located(*web_element))

    def click_element(self, *web_element):
        self.log.info("Finding web element to click....{}".format(web_element))
        self.find_element(*web_element).click()

    # without finding element, perform click action
    # def enter_text(self, web_element, text):
    #     self.log.info("....{}".format(web_element))
    #     web_element.send_keys(text)

    def enter_text(self, text, *web_element):
        self.log.info("Finding web element ....{}".format(web_element))
        self.find_element(*web_element).clear()
        self.find_element(*web_element).send_keys(text)

    def get_text(self, *web_element):
        self.log.info("Finding web element to get text ....{}".format(web_element))
        return self.find_element(*web_element).text

    def open(self, url):
        self.log.info("Open url ...{}".format(url))
        self.driver.get(url)




