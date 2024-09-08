import pytest

from pages.homePage import HomePage
from pages.signInForm import SignInForm


class BaseTest:
    home_page: HomePage
    sign_in_form: SignInForm

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.home_page = HomePage(driver)
        request.cls.sign_in_form = SignInForm(driver)
