from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage


class PimPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    pim_menu_xpath = "//span[text()='PIM']"
    add_button_xpath = "//div[@class='orangehrm-header-container']//button"
    first_name_field_name = "firstName"
    last_name_field_name = "lastName"
    emp_id_field_xpath = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
    save_button_xpath = "//button[text()=' Save ']"
    employee_list_header_link_text = "Employee List"
    employee_name_field_xpath = "//input[@placeholder='Type for hints...']"
    search_button_xpath = "//button[text()=' Search ']"
    number_of_record_found_xpath = "(//span[@class='oxd-text oxd-text--span'])[1]"
    edit_emp_first_name_xpath = "//div[contains(text(),'first_')]"
    edit_save_button_xpath = "(//button[normalize-space()='Save'])[1]"
    retrieve_first_name_xpath = "(//div[@class='oxd-table-cell oxd-padding-cell'])[3]"
    trash_icon_xpath = "(//i[@class='oxd-icon bi-trash'])"
    yes_delete_button_xpath = "//button[normalize-space()='Yes, Delete']"

    def click_pim_menu(self):
        self.element_click("pim_menu_xpath", self.pim_menu_xpath)

    def click_add_button(self):
        self.element_click("add_button_xpath", self.add_button_xpath)

    def enter_all_fields_click_save(self, firstname, lastname, emp_id):
        self.type_into_element(firstname, "first_name_field_name", self.first_name_field_name)
        self.type_into_element(lastname, "last_name_field_name", self.last_name_field_name)
        self.type_into_element(emp_id, "emp_id_field_xpath", self.emp_id_field_xpath)
        self.element_click("save_button_xpath", self.save_button_xpath)

    def click_employee_list(self):
        self.element_click("employee_list_header_link_text", self.employee_list_header_link_text)

    def enter_firstname_click_search(self, text):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, self.employee_name_field_xpath)))
        self.type_into_element(text, "employee_name_field_xpath", self.employee_name_field_xpath)
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.search_button_xpath)))
        self.element_click("search_button_xpath", self.search_button_xpath)

    def check_actual_record_found(self, exp_record_found):
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element((By.XPATH, self.number_of_record_found_xpath), exp_record_found))
        return self.get_element("number_of_record_found_xpath", self.number_of_record_found_xpath).text

    def click_to_edit_emp_first_name(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.edit_emp_first_name_xpath)))
        self.element_click("edit_emp_first_name_xpath", self.edit_emp_first_name_xpath)

    def enter_first_name(self, firstname):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, self.first_name_field_name)))
        element = self.get_element("first_name_field_name", self.first_name_field_name)
        ActionChains(self.driver).move_to_element(element).click(element).perform()
        element.send_keys(firstname)

    def click_edit_save_button(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.edit_save_button_xpath)))
        self.element_click("edit_save_button_xpath", self.edit_save_button_xpath)

    def retrieve_first_name(self):
        return self.get_element("retrieve_first_name_xpath", self.retrieve_first_name_xpath).text

    def click_delete(self):
        self.element_click("trash_icon_xpath", self.trash_icon_xpath)
        self.element_click("yes_delete_button_xpath", self.yes_delete_button_xpath)

    def refresh_page(self):
        self.driver.refresh()