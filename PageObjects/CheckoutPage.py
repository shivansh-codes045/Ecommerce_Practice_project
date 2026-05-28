from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PageObjects.ProductDetailPage import ProductDetailPage
from PageObjects.LoginPage import LoginPage
from PageObjects.BasePage import BasePage
from selenium.webdriver.common.by import By
from PageObjects.HomePage import HomePage
import time
import pytest

class CheckoutPage(BasePage):
    items_in_checkout = []
    def get_matching_product_name(self, product_name):
        self.waiting_for_loader_to_disappear()
        time.sleep(5)
        all_items_in_checkout = self.driver.find_elements(By.XPATH, "//div[contains(@class,'cart_product_list')]//li[contains(@class,'items')]")
        for item in all_items_in_checkout:
            product_name_element = item.find_element(By.XPATH, ".//div[@class='product_detail']/h5")
            print("Product Name in Checkout:", product_name_element.text.strip())
            print("Expected Product Name:", product_name)
            product_name = self.normalize_text(product_name)
            product_name_in_checkout = self.normalize_text(product_name_element.text.strip())
            print("Normalized Product Name in Checkout:", product_name_in_checkout)
            print("Normalized Expected Product Name:", product_name)
            if product_name_in_checkout in product_name:
                print(f"Product name '{product_name_element.text.strip()}' in checkout contains expected product name '{product_name}'")
                break
                

    def get_matching_product_price(self, product_price):
        all_items_in_checkout = self.driver.find_elements(By.XPATH, "//div[contains(@class,'cart_product_list')]//li[contains(@class,'items')]")
        for item in all_items_in_checkout:
            product_price_element = item.find_element(By.XPATH, ".//div[@class='one_prduct_price']/span")
            print("Product Price in Checkout:", product_price_element.text.strip())
            print("Expected Product Price:", product_price)
            if product_price_element.text.strip() in product_price:
                print(f"Product price '{product_price_element.text.strip()}' in checkout matches expected product price '{product_price}'")
            else:
                print("Error")

    def get_all_products_from_checkout(self):
        self.items_in_checkout = []
        self.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'cart_product_list')]//li[contains(@class,'items')]"))
        all_items_in_checkout = self.driver.find_elements(By.XPATH, "//div[contains(@class,'cart_product_list')]//li[contains(@class,'items')]")
        if len(all_items_in_checkout) >= 1:
            for item in all_items_in_checkout:
                product_name_element = item.find_element(By.XPATH, ".//div[@class='product_detail']/h5")
                print("Product Name in Checkout:", product_name_element.text.strip())
                product_price_element = item.find_element(By.XPATH, ".//div[@class='one_prduct_price']/span")
                print("Product Price in Checkout:", product_price_element.text.strip())
                product_details = {"name": product_name_element.text.strip(), "price": product_price_element.text.strip()}
                self.items_in_checkout.append(product_details)
            return self.items_in_checkout
        else:
            print("No item is present in checkout")
            return []   