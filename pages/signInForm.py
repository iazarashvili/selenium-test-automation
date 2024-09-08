import time

from base.base_page import BasePage
from config.url import Urls
from selenium.webdriver.support import expected_conditions as EC


class SignInForm(BasePage):

    input_user_name_field = ('xpath', '//app-new-input/input["autocomplete()=username"][1]')

    def input_username(self, user_name):
        input_name = self.wait.until(EC.element_to_be_clickable(self.input_user_name_field))
        input_name.send_keys(user_name)
