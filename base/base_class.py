import datetime
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class Base():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    """Метод получение текущей юрл"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Corrent url " + get_url)

    """Метод создания скриншотов"""
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d - %H.%M.%S")
        self.driver.save_screenshot(f".\\screen\\screenshot{now_date}.png")

    """Метод проверки url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result, f"{get_url}"
        print("good url")

        """Метод для работы со списком select"""
    def select_option_by_visible_text(self, locator, value):
        select_element = self.wait.until(EC.visibility_of_element_located(locator))
        select = Select(select_element)
        select.select_by_visible_text(value)

        """Метод получение значения из списка select"""
    def get_selected_option_text(self, locator):
        select_element = self.wait.until(EC.visibility_of_element_located(locator))
        selected_option = Select(select_element).first_selected_option
        value = selected_option.text

    """Метод для отображение ошибки"""
    def get_error_value(self, locator):
        locator_value = self.wait.until(
            EC.visibility_of_element_located(locator))
        value_error = locator_value.text
        if any(error in locator for error in locator):
            print("Поле содержит ошибку", f"{value_error}")
        else:
            print("Поле не содержит ни одной из ошибок")

    """Метод для клика"""
    def click(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator)).click()

    """Метод для ввода данных в поля"""
    def input(self, locator, text):
        return self.wait.until(EC.element_to_be_clickable(locator)).send_keys(text)

    """Метод для проверки значения в выпадающем списке select"""
    def assert_value_select(self, locator, expected_value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        selected_value = Select(element).first_selected_option.get_attribute("value")
        selected_value = element.get_attribute("value")
        assert selected_value == expected_value, f"{selected_value}"

    def assert_value_select_text(self, locator, expected_value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        text_content = element.text.strip()
        assert text_content.startswith(expected_value), f"Expected: {expected_value}, Actual: {text_content}"
        assert text_content == expected_value, f"{text_content}"

    """Метод для проверки значения в полях"""
    def assert_value_input(self, locator, expected_value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        input_value = element.get_attribute("value")
        assert input_value == expected_value, f"{input_value}"

    """Метод для проверки что чек бокс активен"""
    def assert_checkbox(self, locator):
        checkbox = self.wait.until(EC.visibility_of_element_located(locator))
        assert checkbox.is_selected()

    """Метод для очистки полей"""
    def clear_value_fields(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).clear()

    def get_value(self, locator):
        locator_1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        text = locator_1.text
        print(text)

    def get_value_1(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        text = element.get_attribute("value")
        print(text)

    """Метод для добавления множества дополнительных полей блоков с одним полем напрмер Цели курса"""
    def add_extra_field(self, quantity, locator_button, locator_filed, text):
        short_locator_filed = locator_filed
        index = 1
        number_value = 0
        for i in range(quantity):
            locator_filed = (By.XPATH, short_locator_filed + f"[{index}]")
            number_value += 1
            index += 1
            self.click(locator_button)
            self.input(locator_filed, text + str(f"{number_value}"))

    """Метод для добавления множества дополнительных полей блоков с двумя полям напрмер результаты обучения
"""
    def add_extra_fields(self, quantity, locator_button, locator_filed_title, locator_filed_text, text_title,
                         text_text):
        short_locator_filed_title = locator_filed_title
        short_locator_filed_text = locator_filed_text
        index = 1
        number_value = 0
        for i in range(quantity):
            locator_filed_title = (By.XPATH, short_locator_filed_title + f"[{index}]")
            locator_filed_text = (By.XPATH, short_locator_filed_text + f"[{index}]")
            number_value += 1
            index += 1
            self.click(locator_button)
            self.input(locator_filed_title, text_title + str(f"{number_value}"))
            self.input(locator_filed_text, text_text + str(f"{number_value}"))

    """Метод для проверки что практика добавилась"""
    def check_practice(self, name_of_practice):
        var_lokator = (By.XPATH, f"//p[contains(text(),'{name_of_practice}')]")
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(var_lokator))
        text_element = element.text
        print(f"Практика {text_element} добавлена")


