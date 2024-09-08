from pages.homePage import HomePage
import time


def test_open_home_age(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_sign_in_button()
    time.sleep(4)

