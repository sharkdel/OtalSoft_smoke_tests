import pytest
from _pytest.fixtures import SubRequest
from allure_commons import fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.ie.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(autouse=True)
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    #driver.set_window_size(1080, 800)
    driver.maximize_window()
    yield driver
    driver.quit()

# @pytest.fixture()
# def driver(request:SubRequest):
#     driver = webdriver.Firefox()
#     driver.quit()

