from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest
from PageObjects.BasePage import BasePage

class ProductDetailPage(BasePage):
    def get_product_name(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'product_discription')]/h5")))
        product_name_element = self.driver.find_element(By.XPATH, "//div[contains(@class,'product_discription')]/h5")   
        return product_name_element.text.strip()

    def get_product_price(self):
        product_name_element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sell_price.fw-bold.text-green")))
        return product_name_element.text.strip()
    
    def click_on_add_to_cart_button(self):
        self.click_element((By.XPATH, "(//button[contains(@class,'add_cart_btn')])[1]"))

    def added_product_to_cart_successfully(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'jq-toast-heading')]")))
        toast_message_element = self.driver.find_element(By.XPATH, "//div[contains(@class,'toast-message')]")
        return toast_message_element.text.strip() == "Product added to cart successfully"
    
    def open_cart_page(self):
        self.click_element((By.XPATH, "//li[@class='cart_btn']/a"))

