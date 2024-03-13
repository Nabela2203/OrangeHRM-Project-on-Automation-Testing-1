from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators in LoginPage
    user_name_field_name = "username"
    password_field_name = "password"
    login_button_xpath = "//button[text()=' Login ']"
    invalid_credentials_text_xpath = "//p[text()='Invalid credentials']"

    def click_login_button(self, username, password):  # Enter username, password and click Login button
        self.type_into_element(username, "user_name_field_name", self.user_name_field_name)
        self.type_into_element(password, "password_field_name", self.password_field_name)
        self.element_click("login_button_xpath", self.login_button_xpath)

    def check_invalid_credentials(self):  # To retrieve text
        self.retrieve_element_text("invalid_credentials_text_xpath", self.invalid_credentials_text_xpath)