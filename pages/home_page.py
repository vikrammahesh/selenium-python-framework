from selenium.webdriver.common.by import By

from Utilities.action_utils import ActionUtils
from pages.shop_page import ShopPage


class HomePage(ActionUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    shop_link = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name ='name']")
    email = (By.NAME, "email")
    pwd = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    emp_radio = (By.CSS_SELECTOR, "label[for='inlineRadio2']")
    submit = (By.CSS_SELECTOR, "input[value='Submit']")
    success_msg = (By.CLASS_NAME, "alert-success")

    def click_shop(self):
        self.driver.find_element(*HomePage.shop_link).click()
        return ShopPage(self.driver)

    def enter_name(self, text):
        self.enter_text(text, *HomePage.name)

    def enter_email(self, text):
        self.enter_text(text, *HomePage.email)

    def check_ice_cream(self):
        self.click_element(*HomePage.checkbox)

    def select_gender(self, text):
        self.select_option_by_text(text, *HomePage.gender)

    def click_emp(self):
        return self.click_element(*HomePage.emp_radio)

    def click_submit(self):
        return self.click_element(*HomePage.submit)

    def get_success_msg(self):
        return self.get_text(*HomePage.success_msg)

    # def get_name(self):
    #     return self.driver.find_element(*HomePage.name)
    #
    # def get_email(self):
    #     return self.driver.find_element(*HomePage.email)
    #
    # def get_check_box(self):
    #     return self.driver.find_element(*HomePage.checkbox)
    #
    # def get_name(self):
    #     return self.driver.find_element(*HomePage.name)
    #
    # def get_gender(self):
    #     return self.driver.find_element(*HomePage.gender)
    #
    # def get_emp(self):
    #     return self.driver.find_element(*HomePage.emp_radio)
    #
    # def get_submit(self):
    #     return self.driver.find_element(*HomePage.submit)
