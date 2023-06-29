from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from utilities.base_class import BaseClass


class MyBooksPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.books_body_locator = (By.ID,"booksBody")
        self.books_list_locator = (By.TAG_NAME, "tr")
        self.cross_button_locator = (By.CSS_SELECTOR, "a[class*='deleteLink']")
        self.empty_book_list_locator = (By.XPATH,"//div[contains(@class,'nocontent')]")
        self.profile_button_locator = (By.CSS_SELECTOR, "div[class*='dropdown--profileMenu']")
        self.sign_out_locator = (By.XPATH, "//a[normalize-space()='Sign out']")

    def get_books_list(self):
        books_body = self.driver.find_element(*self.books_body_locator)
        books_list = books_body.find_elements(*self.books_list_locator)
        return books_list

    def get_cross_button(self,element):
        return element.find_element(*self.cross_button_locator)

    def remove_book(self,book_name):
        self.wait_for_element_visibility(self.books_body_locator, 10)
        books_list = self.get_books_list()
        for book in books_list:
            book_title = book.text.split("\n")[0]
            if book_name.lower() in book_title.lower():
                delete_book = self.get_cross_button(book)
                delete_book.click()
                break

        alert = Alert(self.driver)
        alert.accept()

    def check_book_in_list(self,book_name):
        if not self.check_empty_book_list():
            self.wait_for_element_visibility(self.books_body_locator, 10)
            books_list = self.get_books_list()
            for book in books_list:
                book_title = book.text.split("\n")[0]
                if book_name.lower() in book_title.lower():
                    return True
            return False
        else:
            return True

    def check_empty_book_list(self):
        try:
            self.wait_for_element_visibility(self.empty_book_list_locator, 3)
        except:
            return False
        return True

    def click_profile(self):
        profile_button = self.driver.find_element(*self.profile_button_locator)
        profile_button.click()

    def sign_out(self):
        self.wait_for_element_visibility(self.sign_out_locator)
        sign_out = self.driver.find_element(*self.sign_out_locator)
        sign_out.click()
