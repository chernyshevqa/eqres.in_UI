from pajes.main_page import TestMainPage


def test_check_json_in_other_tab(setup_chrome_driver):
    driver = setup_chrome_driver
    check_json_in_other_tab = TestMainPage(driver)
    check_json_in_other_tab.test_check_json_in_other_tab()
