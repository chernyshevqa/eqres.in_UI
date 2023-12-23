import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from base.base_class import Base

"""Главная страница сайта"""


class TestMainPage(Base):
    url = 'https://reqres.in'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Локаторы"""
    get_list_user = (By.XPATH, "//li[@class='active']")
    get_single_user = (By.XPATH, "//li[@data-id='users-single']")
    get_single_user_not_found = (By.XPATH, "//li[@data-id='users-single-not-found']")
    get_list_resourse = (By.XPATH, "//li[@data-id='unknown']")
    get_single_resourse = (By.XPATH, "//li[@data-id='unknown-single']")
    get_single_resourse_not_found = (By.XPATH, "//li[@data-id='unknown-single-not-found']")
    post_create = (By.XPATH, "//li[@data-id='post']")
    put_update = (By.XPATH, "//li[@data-id='put']")
    patch_update = (By.XPATH, "//li[@data-id='patch']")
    delete = (By.XPATH, "//li[@data-id='delete']")
    post_register_successful = (By.XPATH, "//li[@data-id='register-successful']")
    post_register_unsuccessful = (By.XPATH, "//li[@data-id='register-unsuccessful']")
    post_login_successful = (By.XPATH, "//li[@data-id='login-successful']")
    post_login_unsuccessful = (By.XPATH, "//li[@data-id='login-unsuccessful']")
    get_delayed_responce = (By.XPATH, "//li[@data-id='delay']")
    result_field = (By.XPATH, "//pre[@data-key='output-response']")

    """Методы"""

    def test_get_list_user(self):
        self.click(self.get_list_resourse)
        time.sleep(3)




