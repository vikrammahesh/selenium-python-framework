from selenium.webdriver.common.by import By


class ShopPage:
    product = (By.XPATH, "//div[@class='card h-100']")
    product_name = (By.XPATH, "div/h4/a")
    button = (By.XPATH, "div/button")
    add = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkout = (By.XPATH, "//button[@class='btn btn-success']")
    country = (By.ID, "country")

    def __init__(self, driver):
        self.driver = driver

    def cards(self):
        return self.driver.find_elements(*ShopPage.product)

    def get_product_name(self):
        return self.driver.find_element(*ShopPage.product_name)

    def get_button(self):
        return self.driver.find_element(*ShopPage.button)

    def get_add(self):
        return self.driver.find_element(*ShopPage.add)

    def get_checkout(self):
        return self.driver.find_element(*ShopPage.checkout)

    def get_country(self):
        return self.driver.find_element(*ShopPage.country)
