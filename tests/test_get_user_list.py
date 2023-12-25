from pajes.main_page import TestMainPage


def test_get_user_list(setup_chrome_driver):
    driver = setup_chrome_driver
    get_list_user = TestMainPage(driver)
    get_list_user.test_get_list_user()

