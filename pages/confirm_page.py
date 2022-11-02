from selenium.webdriver.common.by import By


class ConfirmPage:
    india = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH,"//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR,"[type='submit']")
    success_msg = (By.CLASS_NAME,"alert-success")

    def __init__(self, driver):
        self.driver = driver

    def get_india(self):
        return self.driver.find_element(*ConfirmPage.india)

    def get_checkbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def get_submit(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def get_success(self):
        return self.driver.find_element(*ConfirmPage.success_msg)
