from selenium.webdriver.common.by import By
from base.base_class import Base
from examples_responce.example_responce import *

"""Главная страница сайта"""


class TestMainPage(Base):
    url = 'https://reqres.in'

    """Локаторы"""
    get_list_user = (By.XPATH, "//li[@class='active']")
    get_single_user = (By.XPATH, "//li[@data-id='users-single']")
    get_single_user_not_found = (By.XPATH, "//li[@data-id='users-single-not-found']")
    get_list_resource = (By.XPATH, "//li[@data-id='unknown']")
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
    status_code = (By.XPATH, "//span[@class='response-code']")
    result_field = (By.XPATH, "//pre[@data-key='output-response']")
    path = (By.XPATH, "//span[@class='url']")
    other_page_with_json = (By.XPATH, "//pre[@style='word-wrap: break-word; white-space: pre-wrap;']")

    """Методы"""

    def test_get_list_user(self):
        self.driver.get(self.url)
        self.click(self.get_list_user)
        self.get_json(self.result_field, json_get_list_user)
        self.get_text(self.status_code, status_codes["200"])

    def test_get_single_user(self):
        self.driver.get(self.url)
        self.click(self.get_single_user)
        self.get_text(self.status_code, status_codes["200"])

    def test_get_single_user_not_found(self):
        self.driver.get(self.url)
        self.click(self.get_single_user_not_found)
        self.get_text(self.status_code, status_codes["404"]) # тут тест падает потому, что отображает статус код 200 хотя на странице отображается 404

    def test_get_list_resource(self):
        self.driver.get(self.url)
        self.click(self.get_list_resource)
        self.get_json(self.result_field, json_single_resource)
        self.get_text(self.status_code, status_codes["200"])

    def test_get_list_resource_not_found(self):
        self.driver.get(self.url)
        self.click(self.test_get_list_resource_not_found)
        self.get_json(self.result_field, json_single_resource_not_found)
        self.get_text(self.status_code, status_codes["404"])

    def test_get_json_create(self):
        self.driver.get(self.url)
        self.click(self.post_create)
        self.get_json(self.result_field, json_create)
        self.get_text(self.status_code, status_codes["201"])

    def test_get_json_put_update(self):
        self.driver.get(self.url)
        self.click(self.put_update)
        self.get_json(self.result_field, json_update)
        self.get_text(self.status_code, status_codes["200"])

    def test_get_json_patch_update(self):
        self.driver.get(self.url)
        self.click(self.put_update)
        self.get_json(self.result_field, json_update)
        self.get_text(self.status_code, status_codes["200"])

    def test_get_json_delete(self):
        self.driver.get(self.url)
        self.click(self.delete)
        self.get_text(self.status_code, status_codes["200"])

    def test_get_status_code_register(self):
        self.driver.get(self.url)
        self.click(self.post_register_successful)
        self.get_json(self.result_field, json_register_successful)
        self.get_text(self.status_code, status_codes["200"])

    def test_get_status_code_register_unsuccssful(self):
        self.driver.get(self.url)
        self.click(self.post_register_unsuccessful)
        self.get_json(self.result_field, json_register_unsuccessful)
        self.get_text(self.status_code, status_codes["200"])

    def test_get_status_code_login(self):
        self.driver.get(self.url)
        self.click(self.post_login_successful)
        self.get_json(self.result_field, json_login)
        self.get_text(self.status_code, status_codes["200"])

    def test_get_status_code_login_unsuccessful(self):
        self.driver.get(self.url)
        self.click(self.post_login_unsuccessful)
        self.get_json(self.result_field, json_login_unsuccessful)
        self.get_text(self.status_code, status_codes["400"])

    def test_get_status_code_delay_responce(self):
        self.driver.get(self.url)
        self.click(self.get_delayed_responce)
        self.get_json(self.result_field, json_delay_responce)
        self.get_text(self.status_code, status_codes["200"])

    def test_check_json_in_other_tab(self):
        self.driver.get(self.url)
        self.click(self.path)
        self.change_tab(-1)
        self.get_json(self.other_page_with_json, json_get_list_user)
