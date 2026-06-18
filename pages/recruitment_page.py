import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class RecruitmentPage:
    def __init__(self, driver):

        self.driver = driver

        self.recruitment_menu = (By.XPATH, '//span[text()="Recruitment"]')
        self.vacancies_menu = (By.XPATH, "//a[contains(@class,'oxd-topbar-body-nav-tab-item') and normalize-space()='Vacancies']")

        self.add_btn = (By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]')
        self.candidate_firstname_field = (By.XPATH, '//input[@name="firstName"]')
        self.candidate_middlename_field = (By.XPATH, '//input[@name="middleName"]')
        self.candidate_lastname_field = (By.XPATH, '//input[@name="lastName"]')
        self.candidate_email_field = (By.XPATH, '//input[@placeholder="Type here" and class="oxd-input oxd-input--active oxd-input--error"]')
        self.save_btn = (By.XPATH, '//button[@type="submit"]')

    def click_recruitment_menu(self):
        WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.recruitment_menu)).click()

    def click_vacancies_menu(self):
        WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.vacancies_menu)).click()

    def click_add_button(self):
        WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.add_btn)).click()

    def enter_candidate_firstname(self, name):           
        WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.candidate_firstname_field)).send_keys()

    def enter_candidate_middlename(self, name):           
        WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.candidate_middlename_field)).send_keys()

    def enter_candidate_lastname(self, name):           
        WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.candidate_lastname_field)).send_keys()

    def enter_candidate_email(self, name):           
        WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.candidate_email_field)).send_keys()

    def click_save_button(self):
        WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.save_btn)).click()