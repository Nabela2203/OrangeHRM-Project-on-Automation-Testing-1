from configparser import ConfigParser
# config.ini - To remove hard coded data from the automation scripts like url, browser to config.ini file


def read_configuration(category, key):
    config = ConfigParser()
    config.read("configurations/config.ini")
    return config.get(category, key)  # to get data from config.ini file
