from base.base_page import BasePage
from config.url import Urls
from selenium.webdriver.support import expected_conditions as ec


class HomePage(BasePage):
    PAGE_URL = Urls.HOST

    sign_in_button = ('xpath', '//button/span[text()="შესვლა"]')

    def click_sign_in_button(self):
        self.wait.until(ec.element_to_be_clickable(self.sign_in_button)).click()


