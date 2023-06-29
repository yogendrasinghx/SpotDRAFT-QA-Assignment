from selenium.webdriver.common.by import By

from utilities.base_class import BaseClass


class UserHomePage(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.search_book_locator = (By.XPATH,"//div[contains(@class,'searchBox--navbar')]/form/input[@placeholder='Search books']")
        self.search_book_list_locator = (By.XPATH, "//div[contains(@class,'gr-bookSearchResults--navbar')]")

    def type_book_name(self,user_book):
        search_book = self.driver.find_element(*self.search_book_locator)
        search_book.send_keys(user_book)

    def get_books_list(self):
        search_book_list = self.driver.find_element(*self.search_book_list_locator)
        books = search_book_list.find_elements(By.TAG_NAME, "a")
        return books
