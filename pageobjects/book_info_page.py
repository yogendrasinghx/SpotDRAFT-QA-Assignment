from selenium.webdriver.common.by import By

from utilities.base_class import BaseClass


class BookInfoPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.want_to_read_locator = (By.XPATH,"//span[normalize-space()='Want to read']/parent::button[1]")
        self.toast_message_locator = (By.XPATH,"//div[@class='Toastify__toast-body']")
        self.my_books_locator = (By.XPATH, "//a[@href='/review/list?ref=nav_mybooks']")

    def click_want_to_read(self):
        want_to_read = self.driver.find_element(*self.want_to_read_locator)
        want_to_read.click()

    def get_toast_message(self):
        self.wait_for_element_visibility(self.toast_message_locator)
        toast_message = self.driver.find_element(*self.toast_message_locator).text
        return toast_message

    def click_my_books_page_link(self):
        my_books = self.driver.find_element(*self.my_books_locator)
        my_books.click()
