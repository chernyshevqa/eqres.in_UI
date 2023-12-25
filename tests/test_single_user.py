from pajes.main_page import TestMainPage


def test_get_single_user(setup_chrome_driver):
    driver = setup_chrome_driver
    single_user = TestMainPage(driver)
    single_user.test_get_single_user()

