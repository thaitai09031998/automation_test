import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


def test_back(driver):
    print(f"title la : {driver.title}")
    driver.get("https://google.com")
    print(f"title la : {driver.title}")
    driver.back()
    print(f"title la : {driver.title}")




