import random
import allure
import pytest
from base.base_test import BaseTest

@allure.feature("OpenPage Functionality")
class TestOpenPageFeature(BaseTest):

    @allure.title("Open Page name")
    @allure.severity("Critical")
    def test_open_page(self):
        self.login_page.open()
        # self.login_page.enter_login(self.data.LOGIN)
        # self.login_page.enter_password(self.data.PASSWORD)
        # self.login_page.click_submit_button()
        # self.dashboard_page.is_opened()