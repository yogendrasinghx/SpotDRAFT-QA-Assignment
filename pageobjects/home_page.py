from selenium.webdriver.common.by import By

from utilities.base_class import BaseClass


class HomePage(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_button_locator = (By.XPATH,"//a[@href='/user/sign_in']")

    def click_homepage_sign_in(self):
        sign_in_button = self.driver.find_element(*self.sign_in_button_locator)
        sign_in_button.click()


