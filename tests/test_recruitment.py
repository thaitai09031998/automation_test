import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.recruitment_page import RecruitmentPage
from pages.login_page import LoginPage

class TestRecruitment:

    def test_add_candidate(self, driver):

        login_page = LoginPage(driver)
        login_page.login("Admin", "admin123")
        login_page.is_upgrade_button_displayed()
        
        recruitment_page = RecruitmentPage(driver)
        recruitment_page.click_recruitment_menu()
        recruitment_page.click_add_button()
        recruitment_page.enter_candidate_firstname("Tai")
        recruitment_page.enter_candidate_middlename("Thai")
        recruitment_page.enter_candidate_lastname("Nguyen")
        recruitment_page.enter_candidate_email("nguyenthaitai@gmail.com")
        recruitment_page.click_save_button()

