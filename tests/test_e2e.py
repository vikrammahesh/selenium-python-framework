import allure
from selenium.webdriver.common.by import By

from Utilities import logger_utils
from Utilities.base_test import BaseTest
from pages.confirm_page import ConfirmPage
from pages.home_page import HomePage


class TestE2E(BaseTest):
    log = logger_utils.get_logger()

    @allure.title("Add product to cart")
    @allure.description("Select product from all the products and add it to cart")
    def test_first(self):
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        homepage = HomePage(self.driver)
        shop_page = homepage.click_shop()
        products = shop_page.cards()

        for product in products:
            product_name = product.find_element(By.XPATH, "div/h4/a").text
            self.log.info(product_name)
            if product_name == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        shop_page.get_add().click()
        shop_page.get_checkout().click()
        self.log.info("enter country name as ind")
        shop_page.get_country().send_keys("ind")
        self.action_utils.verify_link_text_presence("India")

        confirm_page = ConfirmPage(self.driver)
        confirm_page.get_india().click()
        confirm_page.get_checkbox().click()
        confirm_page.get_submit().click()
        success_text = confirm_page.get_success().text
        self.log.info("Text received from app "+success_text)
        assert "Success! Thank you!" in success_text
        self.driver.close()



















