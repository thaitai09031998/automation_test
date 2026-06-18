import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage
from ultils.config_reader import ConfigReader
class TestLogin:

    def test_login(seft, driver):
        login_page = LoginPage(driver)
        login_page.login(ConfigReader.get_username(), ConfigReader.get_password())
        assert login_page.is_upgrade_button_displayed()
        

