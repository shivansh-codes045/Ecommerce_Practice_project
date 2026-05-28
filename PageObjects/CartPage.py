from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PageObjects.ProductDetailPage import ProductDetailPage
from PageObjects.LoginPage import LoginPage
from PageObjects.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.HomePage import HomePage
import time
import pytest

class CartPage(BasePage):
    items_in_cart = []

    def get_matching_product_name(self, product_name):
        self.waiting_for_loader_to_disappear()
        all_items_in_cart = self.driver.find_elements(By.XPATH, "//div[contains(@class,'cart_product_list')]//li[contains(@class,'items')]")
        for item in all_items_in_cart:
            product_name_element = item.find_element(By.XPATH, ".//div[@class='product_detail']/h5")
            assert product_name_element.text.strip() == f'{product_name}'

    def get_matching_product_price(self, product_price):
        all_items_in_cart = self.driver.find_elements(By.XPATH, "//div[contains(@class,'cart_product_list')]//li[contains(@class,'items')]")
        for item in all_items_in_cart:
            product_price_element = item.find_element(By.XPATH, ".//div[@class='one_prduct_price']/span")
            assert product_price_element.text.strip() == f'{product_price}'

    def increase_product_quantity_in_cart(self, product_name):
        all_items_in_cart = self.driver.find_elements(By.XPATH, "//div[contains(@class,'cart_product_list')]//li[contains(@class,'items')]")
        for item in all_items_in_cart:
            product_name_element = item.find_element(By.XPATH, ".//div[@class='product_detail']/h5")
            if f'{product_name}' in product_name_element.text.strip():
                number_text = item.find_element(By.XPATH,".//input[@type='number']")
                number = number_text.get_attribute('value')
                if int(number) > 1:
                    before_quanity = number
                    print("Quantity before decreasing:", before_quanity)
                    increase_button = item.find_element(By.XPATH, ".//button[normalize-space()='+']")
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", increase_button)
                    increase_button.click()
                    self.waiting_for_loader_to_disappear()
                    after_quantity = item.find_element(By.XPATH,".//input[@type='number']")
                    after = number_text.get_attribute('value')
                    print("Quantity after increasing:", after)
        return {"before": before_quanity, "after": after}

    def decrease_product_quantity_in_cart_where_quantity_is_greater_than_one(self, product_name):
        all_items_in_cart = self.driver.find_elements(By.XPATH, "//div[contains(@class,'cart_product_list')]//li[contains(@class,'items')]")
        for item in all_items_in_cart:
            product_name_element = item.find_element(By.XPATH, ".//div[@class='product_detail']/h5")
            if f'{product_name}' in product_name_element.text.strip():
                number_text = item.find_element(By.XPATH,".//input[@type='number']")
                number = number_text.get_attribute('value')
                if int(number) > 1:
                    before_quanity = number
                    print("Quantity before decreasing:", before_quanity)
                    decrease_button = item.find_element(By.XPATH, ".//button[normalize-space()='-']")
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", decrease_button)
                    decrease_button.click()
                    self.waiting_for_loader_to_disappear()
                    after_quanity = item.find_element(By.XPATH,".//input[@type='number']")
                    after = after_quanity.get_attribute("value")
                    print("Quantity after decreasing:", after)
                    
                else:
                    print("Quantity is 1, cannot decrease further")
                    break

        return {"before": before_quanity, "after": after}

    def decrease_product_quantity_in_cart_where_quantity_is_equal_to_one(self, product_name):
        self.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'cart_product_list')]//li[contains(@class,'items')]"))
        all_items_in_cart = self.driver.find_elements(By.XPATH, "//div[contains(@class,'cart_product_list')]//li[contains(@class,'items')]")
        print(all_items_in_cart)
        for item in all_items_in_cart:
            product_name_element = item.find_element(By.XPATH, ".//div[@class='product_detail']/h5")
            print("product_name_element is =",product_name_element.text.strip(),"product name is =",product_name)
            if f'{product_name}' in product_name_element.text.strip():
                number_text = item.find_element(By.XPATH,".//input[@type='number']")
                number = number_text.get_attribute('value')
                print("number is =",number)
                if int(number) == 1:
                    before_quanity = number
                    print("Quantity before decreasing:", number)
                    decrease_button = item.find_element(By.XPATH, ".//button[normalize-space()='-']")
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", decrease_button)
                    self.driver.execute_script("arguments[0].click()",decrease_button)
                    self.waiting_for_loader_to_disappear()
                    after_number = item.find_element(By.XPATH,".//input[@type='number']")
                    after = after_number.get_attribute("value")
                    print("Quantity after decreasing:", number)
                
            else:
                print("error")
        return {"before": number, "after": after}

    def get_total_item_price_in_cart(self):
        self.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'total_product_ptice')]"))
        all_items_in_cart = self.driver.find_elements(By.XPATH, "//div[contains(@class,'total_product_ptice')]")
        total_price = 0
        for items in all_items_in_cart:
            total_price = total_price + float(items.text.strip().replace(",",""))
        return total_price
            
    def get_total_price_in_bill(self):
        total_price_element = self.driver.find_element(By.XPATH, "//table//td[contains(@class,'item-price-div')]")
        return float(total_price_element.text.strip().replace(",",""))
    
    def checkout_on_cart_page(self):
        self.presence_of_element_located((By.XPATH, "//a[normalize-space()='Checkout']"))
        checkout_button = self.driver.find_element(By.XPATH, "//a[normalize-space()='Checkout']")
        time.sleep(5)
        # ActionChains(self.driver).move_to_element(checkout_button).perform()
        self.driver.execute_script("arguments[0].scrollBy(0, document.body.scrollHeight);", checkout_button)
        try:
            checkout_button.click()
        except Exception as e:
            print("Exception occurred while clicking checkout button:", e)
            
        self.driver.execute_script('arguments[0].click();', checkout_button)
        self.waiting_for_loader_to_disappear()

    def get_all_products_from_cart(self):
        self.items_in_cart = []
        self.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'cart_product_list')]//li[contains(@class,'items')]"))
        all_items_in_cart = self.driver.find_elements(By.XPATH, "//div[contains(@class,'cart_product_list')]//li[contains(@class,'items')]")
        print(all_items_in_cart)
        if len(all_items_in_cart) >= 1:
            for item in all_items_in_cart:
                product_name_element = item.find_element(By.XPATH, ".//div[@class='product_detail']/h5")
                print("Product Name in Cart:", product_name_element.text.strip())
                product_price_element = item.find_element(By.XPATH, ".//div[@class='one_prduct_price']/span")
                print("Product Price in Cart:", product_price_element.text.strip())
                product_details = {"name": product_name_element.text.strip(), "price": product_price_element.text.strip()}
                self.items_in_cart.append(product_details)
            return self.items_in_cart
        else:
            print("No item is present in cart")
            return []
        
        

    def remove_product_from_cart(self, product_name):
        all_items_in_cart = self.driver.find_elements(By.XPATH, "//div[contains(@class,'cart_product_list')]//li[contains(@class,'items')]")
        if len(all_items_in_cart) == 0:
            print("No items in cart to remove")
            return
        elif len(all_items_in_cart) > 0:
            for item in all_items_in_cart:
                product_name_element = item.find_element(By.XPATH, ".//div[@class='product_detail']/h5")
                print("Product Name in Cart for Removal:", product_name_element.text.strip())
                if f'{product_name}' in product_name_element.text.strip():
                    total_products_in_cart = len(all_items_in_cart)
                    remove_button = item.find_element(By.XPATH, ".//button[contains(@class,'remove-cart-item')]")
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", remove_button)
                    self.driver.execute_script('arguments[0].click();', remove_button)
                    self.waiting_for_loader_to_disappear()
                    print(f"Product '{product_name}' removed from cart")
                    self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'cart_product_remove_modal')]")))
                    remove_confirmation_button = self.driver.find_element(By.XPATH, "(//div[contains(@class,'cart_product_remove_modal')]//button[contains(text(),'Yes, Remove')])[2]")
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", remove_confirmation_button)
                    self.driver.execute_script('arguments[0].click();', remove_confirmation_button)
                    self.waiting_for_loader_to_disappear()
                    self.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'cart_product_list')]//li[contains(@class,'items')]"))
                    remaining_products_in_cart = len(self.driver.find_elements(By.XPATH, "//div[contains(@class,'cart_product_list')]//li[contains(@class,'items')]"))
                    return {"before": total_products_in_cart, "after": remaining_products_in_cart}
                else:
                    print(f"Product '{product_name}' not found in cart")

    def empty_cart(self):
        all_items_in_cart = self.driver.find_elements(By.XPATH, "//div[contains(@class,'cart_product_list')]//li[contains(@class,'items')]")
        if len(all_items_in_cart) > 0:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", self.driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Clear Cart')]"))
            self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Clear Cart')]"))
            self.waiting_for_loader_to_disappear()
            time.sleep(2)
            remove_confirmation_button = self.driver.find_element(By.XPATH, "(//div[contains(@class,'cart_product_remove_modal')]//button[contains(text(),'Yes, Remove')])[2]")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", remove_confirmation_button)
            self.driver.execute_script('arguments[0].click();', remove_confirmation_button)
            self.waiting_for_loader_to_disappear()
            self.presence_of_element_located((By.XPATH, "//h3[normalize-space()='Your cart is empty.']"))
            assert self.driver.find_element(By.XPATH, "//h3[normalize-space()='Your cart is empty.']").is_displayed()
        elif len(all_items_in_cart) == 0:
            print("Nothing Present in cart")
    
    def is_checkout_button_present(self):
        checkout_button = self.driver.find_elements(By.XPATH, "//a[normalize-space()='Checkout']")
        return len(checkout_button) > 0