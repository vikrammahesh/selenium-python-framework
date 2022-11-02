import allure
import pytest

from Utilities import logger_utils
from Utilities.base_test import BaseTest
from pages.home_page import HomePage
from test_data.home_page_test_data import HomePageTestData


class TestHome(BaseTest):
    log = logger_utils.get_logger()

    @allure.title("Submit form")
    @allure.description("Submit a user with different data")
    def test_form_submission(self, get_users):
        self.action_utils.open(self.get_env_value('url'))
        home_page = HomePage(self.driver)
        home_page.enter_name(get_users['firstname'])
        self.log.info("Enter name " + get_users['firstname'])
        home_page.enter_email(get_users['lastname'])
        home_page.check_ice_cream()
        home_page.select_gender(get_users['gender'])
        home_page.click_emp()
        home_page.click_submit()
        message_text = home_page.get_success_msg()
        self.log.info("Alter message " + message_text)
        assert "Success" in message_text

        # another version of scripting
        # self.action_utils.enter_text(home_page.get_name(), get_users['firstname'])
        # self.action_utils.enter_text(home_page.get_email(), get_users['lastname'])
        # self.action_utils.click_element(home_page.get_email())
        # self.action_utils.select_option_by_text(home_page.get_gender(), get_users['gender'])
        # self.action_utils.click_element(home_page.get_emp())
        # self.action_utils.click_element(home_page.get_submit())
        # message_text = self.action_utils.get_text(home_page.get_success_msg())
        # self.log.info("Alter message " + message_text)
        # assert "Success" in message_text

    # () - tuple can pass the values
    # dictionary{} can pass values as key value pairs
    @pytest.fixture(params= HomePageTestData.home_page_test_data)
    def get_users(self, request):
        return request.param

    @allure.title("Test success")
    def test_success(self):
        """this tests succeeds"""
        assert True

    @allure.title("Test Failure")
    def test_failure(self):
        """this tests fails"""
        assert False

    @allure.title("Test SKIP")
    def test_skip(self):
        """this tests is skipped"""
        pytest.skip('for a reason!')

    @allure.title("Test Broken")
    def test_broken(self):
        raise Exception('oops')

    @allure.title("Env variable")
    def test_env(self):
        u, p = self.get_env_vars()
        assert u == 'test'
        assert p == 'xxx'

    @allure.title("read json data ")
    def test_data(self):
        self.log.info(self.get_data())
        self.log.info(self.CONSTANTS['practice'][1]['name'])

