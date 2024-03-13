from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException,
    WebDriverException,
    InvalidSelectorException
)

# TC_Login_01 : Successful Employee login to OrangeHRM portal


class TestLogin(BaseTest):

    def test_login_with_valid_username_and_valid_password(self):  # Testing with valid username and valid password

        try:
            # Go to LoginPage to access driver
            login_page = LoginPage(self.driver)
            # Enter username, password and click login button
            login_page.click_login_button("Admin", "admin123")

            exp_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
            # condition - to check current url = expected url
            assert self.driver.current_url == exp_url

        except (NoSuchElementException, TimeoutException, StaleElementReferenceException, WebDriverException,
                InvalidSelectorException) as e:
            print(f"Exception occurred: {type(e).__name__}: {e}")
            return None  # any default value suitable for your case

    # TC_Login_02: Invalid Employee Login to OrangeHRM portal

    def test_login_with_valid_username_and_invalid_password(self):  # Testing with valid username and invalid password

        try:
            # Go to LoginPage to access driver
            login_page = LoginPage(self.driver)
            # Enter username, password and click login button
            login_page.click_login_button("Admin", "admin")

            actual_text = login_page.check_invalid_credentials()
            exp_text = "Invalid credentials"
            # condition - to check actual text = expected text
            assert actual_text.__eq__(exp_text)

        except (NoSuchElementException, TimeoutException, StaleElementReferenceException, WebDriverException,
                InvalidSelectorException) as e:
            print(f"Exception occurred: {type(e).__name__}: {e}")
            return None  # any default value suitable for your case