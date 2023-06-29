from selenium.webdriver.common.by import By

from utilities.base_class import BaseClass


class SignInPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_with_email_locator = (By.XPATH,"//button[normalize-space()='Sign in with email']")
        self.email_locator = (By.ID,"ap_email")
        self.password_locator = (By.ID,"ap_password")
        self.sign_in_button_locator = (By.ID, "signInSubmit")



    def click_sign_in_with_email(self):
        sign_in_button = self.driver.find_element(*self.sign_in_with_email_locator)
        sign_in_button.click()

    def type_email(self,user_email):
        email = self.driver.find_element(*self.email_locator)
        email.send_keys(user_email)

    def type_password(self,user_password):
        password = self.driver.find_element(*self.password_locator)
        password.send_keys(user_password)

    def click_sign_in(self):
        sign_in = self.driver.find_element(*self.sign_in_button_locator)
        sign_in.click()



