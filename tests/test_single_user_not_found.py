from pajes.main_page import TestMainPage


def test_get_single_user_not_found(setup_chrome_driver):
    driver = setup_chrome_driver
    single_user_not_found = TestMainPage(driver)
    single_user_not_found.test_get_single_user_not_found()
