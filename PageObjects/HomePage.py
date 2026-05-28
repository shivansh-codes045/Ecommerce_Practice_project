from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PageObjects.ProductDetailPage import ProductDetailPage
from PageObjects.LoginPage import LoginPage
from PageObjects.BasePage import BasePage
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):

    all_products_added_to_cart = []
    def change_language(self):
        self.click_element((By.ID, "dropdownMenuButton1"))
        self.click_element((By.CSS_SELECTOR, "button[value='English']"))
        time.sleep(5)

    def verify_language_change(self):
        self.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'content_block')]"))
        actual_text = self.driver.find_element(By.CSS_SELECTOR, "button[class='primary_btn']")
        assert actual_text.text == "Sell"

    def from_all_products_select_n_number_of_products(self, n):
        self.all_products_added_to_cart = []
        self.waiting_for_loader_to_disappear()
        self.driver.execute_script('document.body.style.zoom="50%"')
        time.sleep(5)
        self.presence_of_all_elements_located((By.XPATH, "//li[contains(@class,'slick-active') and contains(@class,'product_item')]"))
        all_products = self.driver.find_elements(By.XPATH, "//li[contains(@class,'slick-active') and contains(@class,'product_item')]")
        for i in range(n):
            product_name = all_products[i].find_element(By.XPATH, ".//a//h5").text.strip()
            product_price = all_products[i].find_element(By.XPATH, ".//a//p/span").text.strip()
            product_button = all_products[i].find_element(By.XPATH, ".//a")
            self.driver.execute_script("arguments[0].scrollIntoView();", all_products[i])
            print(f"Adding product to cart: {product_name} with price: {product_price}")
            ActionChains(self.driver).move_to_element(all_products[i]).perform()
            add_to_cart_button = all_products[i].find_element(By.XPATH, ".//a//div[contains(@class,'product_btn')]//button[contains(@class,'add_cart_btn')]")
            self.waiting_for_loader_to_disappear()
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_cart_button)
            ActionChains(self.driver).move_to_element(add_to_cart_button).perform()
            add_to_cart_button.click()
            self.waiting_for_loader_to_disappear()
            self.added_product_to_cart_successfully()
            product_details = {"name": product_name, "price": product_price}
            self.all_products_added_to_cart.append(product_details)
            print(f"Product added to cart: {self.all_products_added_to_cart}")
            
    def open_product_detail_page_for_product(self,product_name):
        print(f"Opening product detail page for product: {product_name}")
        self.waiting_for_loader_to_disappear()
        self.presence_of_element_located((By.XPATH, f"(//h5[@title='{product_name}'])[2]"))
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.XPATH, f"(//h5[@title='{product_name}'])[2]"))
        self.click_element((By.XPATH, f"(//h5[@title='{product_name}'])[2]"))
        self.waiting_for_loader_to_disappear()
        return ProductDetailPage(self.driver)
    
    def added_product_to_cart_successfully(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,' jq-icon-success')]")))
        toast_message_element = self.driver.find_element(By.XPATH, "//div[contains(@class,' jq-icon-success')]//h2")
        print("Toast message after adding product to cart:", toast_message_element.text.strip())
        assert toast_message_element.text.strip() == "Success!"

    def open_login_page(self):
        print("Opening login page")
        self.click_element((By.CSS_SELECTOR, "a.login_btn.pe-1"))
        return LoginPage(self.driver)
    
    def verify_user_logged_in(self):
        time.sleep(5)
        self.waiting_for_loader_to_disappear()
        self.presence_of_element_located((By.CLASS_NAME, "login_btn"))
        user_name_element = self.driver.find_element(By.XPATH, "//a[contains(@class,'login_btn')]")
        print("Logged in user name:", user_name_element.text)
        if user_name_element.text.strip() == "My Profile":
            print("User logged in successfully")
        else:
            pytest.fail("User login failed")

    def open_cart_page(self):
        self.click_element((By.XPATH, "//li[@class='cart_btn']/a"))
        self.waiting_for_loader_to_disappear()

        