from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://extra.ge/')

    def click_sign_in_button(self):
        sign_in_btn = self.browser.find_element(By.XPATH, '//button/span[text()="შესვლა"]')
        sign_in_btn.click()
