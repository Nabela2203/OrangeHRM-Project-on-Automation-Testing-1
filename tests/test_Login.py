from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest


# TC_Login_01 : Successful Employee login to OrangeHRM portal


class TestLogin(BaseTest):
    def test_login_with_valid_username_and_valid_password(self):

        login_page = LoginPage(self.driver)
        login_page.click_login_button("Admin", "admin123")

        exp_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        assert self.driver.current_url == exp_url

# TC_Login_02: Invalid Employee Login to OrangeHRM portal

    def test_login_with_valid_username_and_invalid_password(self):

        login_page = LoginPage(self.driver)
        login_page.click_login_button("Admin", "admin")

        actual_text = login_page.check_invalid_credentials()
        exp_text = "Invalid credentials"
        assert actual_text.__eq__(exp_text)