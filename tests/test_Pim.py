from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.LoginPage import LoginPage
from pages.PimPage import PimPage
from tests.BaseTest import BaseTest


# TC_PIM_01: Add a new employee in the PIM module

class TestPim(BaseTest):

    def test_add_new_employee(self):
        login_page = LoginPage(self.driver)
        login_page.click_login_button("Admin", "admin123")

        pim_page = PimPage(self.driver)
        pim_page.click_pim_menu()
        pim_page.click_add_button()

        first_name = self.generate_first_name_with_timestamp()
        last_name = self.generate_last_name_with_timestamp()
        employee_id = self.generate_employee_id_with_timestamp()
        pim_page.enter_all_fields_click_save(first_name, last_name, employee_id)

        exp_url = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/"
        WebDriverWait(self.driver, 10).until(EC.url_contains(exp_url))

        pim_page.click_employee_list()
        pim_page.enter_firstname_click_search(first_name)

        actions = ActionChains(self.driver)
        actions.send_keys(Keys.DOWN).perform()

        exp_record_found = "(1) Record Found"
        assert pim_page.check_actual_record_found(exp_record_found) == exp_record_found

# TC_PIM_02: Edit an existing employee in the PIM module

    def test_edit_existing_employee(self):

        login_page = LoginPage(self.driver)
        login_page.click_login_button("Admin", "admin123")

        pim_page = PimPage(self.driver)
        pim_page.click_pim_menu()

        actions = ActionChains(self.driver)
        actions.send_keys(Keys.DOWN).perform()
        pim_page.refresh_page()

        pim_page.click_to_edit_emp_first_name()

        new_first_name = self.generate_first_name_with_timestamp()
        pim_page.enter_first_name(new_first_name)

        actions.send_keys(Keys.DOWN).perform()

        pim_page.click_edit_save_button()

        pim_page.click_employee_list()
        pim_page.refresh_page()
        pim_page.enter_firstname_click_search(new_first_name)

        exp_record_found = "(1) Record Found"
        assert pim_page.check_actual_record_found(exp_record_found) == exp_record_found

# TC_PIM_03: Delete an existing employee in the PIM module

    def test_delete_existing_employee(self):

        login_page = LoginPage(self.driver)
        login_page.click_login_button("Admin", "admin123")

        pim_page = PimPage(self.driver)
        pim_page.click_pim_menu()

        pim_page.click_employee_list()
        pim_page.refresh_page()

        pim_page.enter_firstname_click_search("first")
        first_name_text = pim_page.retrieve_first_name()
        pim_page.click_delete()

        pim_page.click_employee_list()

        pim_page.enter_firstname_click_search(first_name_text)

        exp_record_found = "No Records Found"
        assert pim_page.check_actual_record_found(exp_record_found) == exp_record_found