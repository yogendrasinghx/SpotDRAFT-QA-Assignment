import time
from pageobjects.book_info_page import BookInfoPage
from pageobjects.home_page import HomePage
from pageobjects.my_books_page import MyBooksPage
from pageobjects.sign_in_page import SignInPage
from pageobjects.user_home_page import UserHomePage
from testdata.test_data import data
from utilities.base_class import BaseClass


class TestScenarios(BaseClass):

    def test_homepage_sign_in_button(self):
        home_page = HomePage(self.driver)
        home_page.click_homepage_sign_in()
        title = home_page.get_page_title()
        assert title == "Sign in"

    def test_login(self):

        email = data['email']
        password = data['password']

        signin_page = SignInPage(self.driver)
        signin_page.click_sign_in_with_email()
        signin_page.type_email(email)
        signin_page.type_password(password)
        signin_page.click_sign_in()
        title = signin_page.get_page_title()


        assert title == "Recent updates | Goodreads"

    def test_search_book(self):
        book_name = data['book']
        user_homepage = UserHomePage(self.driver)
        self.wait_for_element_visibility(user_homepage.search_book_locator,5)
        user_homepage.type_book_name(book_name)
        self.wait_for_element_visibility(user_homepage.search_book_list_locator, 5)
        books = user_homepage.get_books_list()
        for book in books:
            book_title = book.text.split("\n")[0]
            if book_name.lower() in book_title.lower():
                book.click()
                break
        title = self.get_page_title()
        assert book_name.lower() in title.lower()

    def test_add_want_to_read_book(self):
        book_info_page = BookInfoPage(self.driver)
        book_info_page.click_want_to_read()
        toast_message = book_info_page.get_toast_message()
        assert toast_message == "Shelved as want to read"


    def test_open_my_books_page(self):
        book_info_page = BookInfoPage(self.driver)
        book_info_page.click_my_books_page_link()
        title = self.get_page_title()
        assert "books on Goodreads" in title

    def test_remove_selected_book(self):
        book_name = data['book']
        my_books_page = MyBooksPage(self.driver)
        my_books_page.remove_book(book_name)
        time.sleep(3)
        assert my_books_page.check_book_in_list(book_name)

    def test_logout(self):
        my_books_page = MyBooksPage(self.driver)
        my_books_page.click_profile()
        my_books_page.sign_out()
        page_url = self.get_current_url()
        assert page_url == "https://www.goodreads.com/"



