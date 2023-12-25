import datetime
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class Base:
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

    """Метод для проверки значения в полях"""
    def assert_value_input(self, locator, expected_value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        input_value = element.get_attribute("value")
        assert input_value == expected_value, f"{input_value}"

    """Метод для получения текста и для смены типа данных и проверка на соответствие json"""
    def get_json(self, locator, expected_result):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        text = element.text #получаем текст ответа
        json_dict = json.loads(text) #меняем тип данных
        assert json_dict == expected_result, f"{json_dict}" #сравниваем фактический и ожидаемые результаты

    """Метод для получение текста и проверки на соответствие"""
    def get_text(self, locator, expected_result):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        text = element.text
        assert text == expected_result, f"Статус код {text}"

    """Метод для переключения на другие вкладки"""
    def change_tab(self, tab_number):
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[tab_number])



