from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest

class BasePage:
    loader_locator = (By.XPATH, "//div[@id='site_loader']/div/img")
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def waiting_for_loader_to_disappear(self):
        self.wait.until(EC.invisibility_of_element_located(self.loader_locator))

    def click_element(self, by_locator):
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        element.click()

    def presence_of_all_elements_located(self, by_locator):
        self.wait.until(EC.presence_of_all_elements_located(by_locator))

    def presence_of_element_located(self, by_locator):
        self.wait.until(EC.presence_of_element_located(by_locator))

    def normalize_text(self, text):
        return ' '.join(text.split())