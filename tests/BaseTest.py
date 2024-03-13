from datetime import datetime
import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class BaseTest:  # BaseTest - Parent class
    def generate_first_name_with_timestamp(self):  # To generate new first name
        timestamp = datetime.now().strftime('%S')
        return "first" + "_" + timestamp

    def generate_last_name_with_timestamp(self):  # To generate new last name
        timestamp = datetime.now().strftime('%S')
        return "last" + "_" + timestamp

    def generate_employee_id_with_timestamp(self):  # To generate new employee ID
        timestamp = datetime.now().strftime('%S')
        return timestamp





