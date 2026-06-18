import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(seft, driver):
        super().__init__(driver)
        
        seft.driver = driver 
        
        seft.username_field = (By.NAME, 'username')
        seft.password_field = (By.NAME, 'password')
        seft.click_btn = (By.XPATH, '//button[@type="submit"]')
        seft.upgrade_btn = (By.XPATH, '//button[@class="oxd-glass-button orangehrm-upgrade-button"]')

    def login(seft, username, password):
        seft.driver.find_element(*seft.username_field).send_keys(username)
        seft.driver.find_element(*seft.password_field).send_keys(password)
        seft.driver.find_element(*seft.click_btn).click()

    def is_upgrade_button_displayed(self):
        return WebDriverWait(self.driver,10).until(lambda d: d.find_element(*self.upgrade_btn).is_displayed())