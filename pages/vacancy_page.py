import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class VacancyPage:
    def __init__(self, driver):

        self.driver = driver

        self.add_btn = (By.XPATH, "//button[@type='button' and .//i[contains(@class,'bi-plus')]]")
        self.vacancy_label = (By.XPATH, "//h6[text()='Add Vacancy']")
        self.vancancy_name_field = (By.XPATH, "//label[text()='Vacancy Name']/following::input[1]")
        self.vancancy_jobtitle_dropdown = (By.XPATH, "//label[text()='Job Title']/following::div[contains(@class,'oxd-select-text')][1]")
        self.vancancy_jobtitle_list = (By.XPATH, "//div[@role='option']/span[text()='Automaton Tester']")
        self.vancancy_description_field = (By.XPATH, "//textarea[@placeholder='Type description here']")
        self.vancancy_username_field = (By.XPATH, "//p[contains(@class,'oxd-userdropdown-name')]")
        self.vancancy_hiringmanager_field = (By.XPATH, "//input[@placeholder='Type for hints...']")

    def click_add_button(self):
        WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.add_btn)).click()

    def display_vacancy_label(self):
        return WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.vacancy_label)).is_displayed()
    
    def enter_vancancy_name(self, name):           
        WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.vancancy_name_field)).send_keys(name)

    def choose_vancancy_jobtitle(self):
        WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.vancancy_jobtitle_dropdown)).click()
        WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.vancancy_jobtitle_list)).click()

    def enter_vancancy_description(self, description):           
        WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.vancancy_description_field)).send_keys(description)

    def enter_vancancy_hiringmanager(self):
        hiringmanager = WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.vancancy_username_field)).text
        WebDriverWait(self.driver, 10).until(lambda d: d.find_element(*self.vancancy_hiringmanager_field)).send_keys(hiringmanager)