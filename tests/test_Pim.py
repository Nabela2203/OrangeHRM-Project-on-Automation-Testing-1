from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.LoginPage import LoginPage
from pages.PimPage import PimPage
from tests.BaseTest import BaseTest
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException,
    WebDriverException,
    InvalidSelectorException
)


# TC_PIM_01: Add a new employee in the PIM module

class TestPim(BaseTest):

    def test_add_new_employee(self):  # To add new employee

        try:
            # Go to LoginPage to access driver
            login_page = LoginPage(self.driver)
            # Enter username, password and click login button
            login_page.click_login_button("Admin", "admin123")

            # Go to PimPage to access driver, click PIM and click add button
            pim_page = PimPage(self.driver)
            pim_page.click_pim_menu()
            pim_page.click_add_button()

            # To generate new first name, last name and employee ID and click save
            first_name = self.generate_first_name_with_timestamp()
            last_name = self.generate_last_name_with_timestamp()
            employee_id = self.generate_employee_id_with_timestamp()
            pim_page.enter_all_fields_click_save(first_name, last_name, employee_id)

            exp_url = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/"
            WebDriverWait(self.driver, 10).until(EC.url_contains(exp_url))

            # Click Employee list
            pim_page.click_employee_list()
            # Enter first name and Search
            pim_page.enter_firstname_click_search(first_name)

            actions = ActionChains(self.driver)
            actions.send_keys(Keys.DOWN).perform()

            exp_record_found = "(1) Record Found"
            # condition - to check actual record found = expected record found
            assert pim_page.check_actual_record_found(exp_record_found) == exp_record_found

        except (NoSuchElementException, TimeoutException, StaleElementReferenceException, WebDriverException,
                InvalidSelectorException) as e:
            print(f"Exception occurred: {type(e).__name__}: {e}")
            return None  # any default value suitable for your case

# TC_PIM_02: Edit an existing employee in the PIM module

    def test_edit_existing_employee(self):  # To edit existing employee

        try:
            # Go to LoginPage to access driver
            login_page = LoginPage(self.driver)
            # Enter username, password and click login button
            login_page.click_login_button("Admin", "admin123")

            # Go to PimPage to access driver and click PIM
            pim_page = PimPage(self.driver)
            pim_page.click_pim_menu()

            actions = ActionChains(self.driver)
            actions.send_keys(Keys.DOWN).perform()
            pim_page.refresh_page()

            # Search name and click edit
            pim_page.click_to_edit_emp_first_name()

            # To generate new first name and enter in the first name field
            new_first_name = self.generate_first_name_with_timestamp()
            pim_page.enter_first_name(new_first_name)

            actions.send_keys(Keys.DOWN).perform()

            # Click save button
            pim_page.click_edit_save_button()

            # To check click Employee List, enter first name and search
            pim_page.click_employee_list()
            pim_page.refresh_page()
            pim_page.enter_firstname_click_search(new_first_name)

            exp_record_found = "(1) Record Found"
            # condition - to check actual record found = expected record found
            assert pim_page.check_actual_record_found(exp_record_found) == exp_record_found

        except (NoSuchElementException, TimeoutException, StaleElementReferenceException, WebDriverException,
                InvalidSelectorException) as e:
            print(f"Exception occurred: {type(e).__name__}: {e}")
            return None  # any default value suitable for your case

# TC_PIM_03: Delete an existing employee in the PIM module

    def test_delete_existing_employee(self):  # To delete Existing employee

        try:
            # Go to LoginPage to access driver
            login_page = LoginPage(self.driver)
            # Enter username, password and click login button
            login_page.click_login_button("Admin", "admin123")

            # Go to PimPage to access driver and click PIM
            pim_page = PimPage(self.driver)
            pim_page.click_pim_menu()

            # Click Employee List
            pim_page.click_employee_list()
            pim_page.refresh_page()

            # Enter 'first' in first name field and click delete
            pim_page.enter_firstname_click_search("first")
            first_name_text = pim_page.retrieve_first_name()
            pim_page.click_delete()

            # Click Employee List
            pim_page.click_employee_list()

            # Enter first name and click search
            pim_page.enter_firstname_click_search(first_name_text)

            exp_record_found = "No Records Found"
            # condition - to check actual record found = expected record found
            assert pim_page.check_actual_record_found(exp_record_found) == exp_record_found

        except (NoSuchElementException, TimeoutException, StaleElementReferenceException, WebDriverException,
                InvalidSelectorException) as e:
            print(f"Exception occurred: {type(e).__name__}: {e}")
            return None  # any default value suitable for your case