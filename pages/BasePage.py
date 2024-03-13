from selenium.webdriver.common.by import By


class BasePage:  # BasePage - parent or base class for all the pages

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator_name, locator_value):  # To retrieve element based on locators
        element = None  # Local variable 'element' might be referenced before assignment, so used element = None
        if locator_name.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.__contains__("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_name.__contains__("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_name.__contains__("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_name.__contains__("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.__contains__("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element

    def type_into_element(self, text, locator_name, locator_value):  # To enter text
        element = self.get_element(locator_name, locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def element_click(self, locator_name, locator_value):  # To click element
        element = self.get_element(locator_name, locator_value)
        element.click()

    def check_display_status_of_element(self, locator_name, locator_value):  # To check element is displayed
        element = self.get_element(locator_name, locator_value)
        return element.is_displayed()

    def check_element_is_enabled(self, locator_name, locator_value):  # To check element is enabled
        element = self.get_element(locator_name, locator_value)
        return element.is_enabled()

    def retrieve_element_text(self, locator_name, locator_value):  # To retrieve text
        element = self.get_element(locator_name, locator_value)
        return element.text