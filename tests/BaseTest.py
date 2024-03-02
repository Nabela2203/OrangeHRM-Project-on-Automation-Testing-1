from datetime import datetime
import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class BaseTest:  # BaseTest - Parent class
    def generate_first_name_with_timestamp(self):
        timestamp = datetime.now().strftime('%S')
        return "first" + "_" + timestamp

    def generate_last_name_with_timestamp(self):
        timestamp = datetime.now().strftime('%S')
        return "last" + "_" + timestamp

    def generate_employee_id_with_timestamp(self):
        timestamp = datetime.now().strftime('%S')
        return timestamp





