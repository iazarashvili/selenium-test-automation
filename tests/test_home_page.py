from base.base_test import BaseTest
import time


class TestHomePage(BaseTest):

    def test_open_home_page(self):
        self.home_page.open()
        self.home_page.click_sign_in_button()
        self.sign_in_form.input_username('ilia')
        time.sleep(4)

