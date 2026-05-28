from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from PageObjects.BasePage import BasePage
from PageObjects.HomePage import HomePage
import pytest
from datetime import datetime

@pytest.fixture(scope="function")
def driver_setup():
    options = Options()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get("https://dev.mustadam.shop/")
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def change_language_and_verify(driver_setup):
        driver = driver_setup
        base_page = BasePage(driver)
        home_page = HomePage(driver)
        base_page.waiting_for_loader_to_disappear()
        home_page.change_language()
        base_page.waiting_for_loader_to_disappear()
        home_page.verify_language_change()
        yield driver
        driver.quit()

@pytest.fixture(scope="session")
def driver_setup1():
    options = Options()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get("https://dev.mustadam.shop/")
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def change_language_and_verify1(driver_setup1):
        driver = driver_setup1
        base_page = BasePage(driver)
        home_page = HomePage(driver)
        base_page.waiting_for_loader_to_disappear()
        home_page.change_language()
        base_page.waiting_for_loader_to_disappear()
        home_page.verify_language_change()
        yield driver
        driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
      outcome = yield
      report = outcome.get_result()
      if report.when == 'call' and report.failed:
            driver = None
            for value in item.funcargs.values():
                  if hasattr(value,'save_screenshot'):
                        driver = value
                        break
            
            if driver:
                  timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                  screenshot_name = (f"screenshots/"f"{item.name}_{timestamp}.png")
                  driver.save_screenshot(screenshot_name)

