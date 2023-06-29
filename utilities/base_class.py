import time

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('setup')
class BaseClass:
    def get_page_title(self):
        time.sleep(2)
        return self.driver.title
    def wait_for_element_visibility(self,locator,time=5):
        wait = WebDriverWait(self.driver,time)
        wait.until(expected_conditions.visibility_of_element_located((locator)))

    def get_current_url(self):
        return self.driver.current_url