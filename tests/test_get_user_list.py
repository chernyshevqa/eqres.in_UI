import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pajes.main_page import TestMainPage


def test_get_user_list():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    get_user_list = TestMainPage(driver)
    get_user_list.test_get_list_user()

    driver.quit()
