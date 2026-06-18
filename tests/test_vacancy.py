import pytest
from selenium import webdriver
from time import sleep
from datetime import date
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage
from pages.vacancy_page import VacancyPage

class TestVacancy:

    def test_display_vacancy(self, driver):
        
        login_page = LoginPage(driver)
        login_page.login("Admin", "admin123")
        login_page.is_upgrade_button_displayed()

        recruitment_page = RecruitmentPage(driver)
        recruitment_page.click_recruitment_menu()
        recruitment_page.click_vacancies_menu()

        vacancy_page = VacancyPage(driver)
        vacancy_page.click_add_button()
        assert vacancy_page.display_vacancy_label()

        today = date.today()
        vacancy_page.enter_vancancy_name(f"Automation Tester For {today} ")

        vacancy_page.choose_vancancy_jobtitle()

        vacancy_page.enter_vancancy_description("Automation Test Is Running")

        vacancy_page.enter_vancancy_hiringmanager()

        sleep(10)
    
