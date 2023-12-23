import pytest

from pajes.main_page import TestMainPage


@pytest.fixture
def test_main_page(request):
    driver = request.param
    test_main_page_instance = TestMainPage(driver)
    return test_main_page_instance