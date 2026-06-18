import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


def test_login(driver):
    username_field = (By.NAME, 'username')
    password_field = (By.NAME, 'password')
    
    click_btn = (By.XPATH, '//button[@type="submit"]')
    upgrade_btn = (By.XPATH, '//button[@class="oxd-glass-button orangehrm-upgrade-button"]')
    recruitment_btn = (By.XPATH, '//a[@href="/web/index.php/recruitment/viewRecruitmentModule"]')
    search_btn = (By.XPATH, '//button[@type="submit"]')

    driver.find_element(*username_field).send_keys('Admin')
    driver.find_element(*password_field).send_keys('admin123')
    driver.find_element(*click_btn).click()

    assert driver.find_element(*upgrade_btn).is_displayed()

    driver.find_element(*recruitment_btn).click()

    driver.find_element(*search_btn).click()
    sleep(5)


