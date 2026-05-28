from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PageObjects import BasePage, HomePage
from selenium.webdriver.common.by import By
import time
import pytest
from PageObjects.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    email_button = (By.XPATH, "//button[@aria-controls='email_login']")
    email_input_button = ()
    def select_email_login_option(self):
        self.waiting_for_loader_to_disappear()
        print("Selecting email login option")
        self.click_element(self.email_button)
        print("Email login option selected")

    def login_with_email_and_password(self, email, password):
        self.presence_of_element_located((By.ID, "email_email"))
        email_input = self.driver.find_element(By.ID, "email_email")
        email_input.send_keys(email)
        pwd_input = self.driver.find_element(By.ID, "password")
        pwd_input.send_keys(password)
        self.click_element((By.ID, "sign_in_btn"))
        

    def get_error_message(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='email-email-error']//li")))
        error_message_element = self.driver.find_element(By.XPATH, "//div[@id='email-email-error']//li")
        print(error_message_element.text.strip())
        return error_message_element.text.strip()


    def verify_successful_login(self):
        self.waiting_for_loader_to_disappear()
        return HomePage(self.driver)
    
    def check_password_field(self):
        self.presence_of_element_located((By.ID, "email_email"))
        pwd_input = self.driver.find_element(By.ID, "password")
        pwd_atr = pwd_input.get_attribute("type")
        print(pwd_atr)
        return pwd_atr
    
    def click_password_eye_button_after_entering_password(self,password):
        self.presence_of_element_located(((By.ID, "password")))
        pwd_input = self.driver.find_element(By.ID, "password")
        pwd_input.send_keys(password)
        eye_button = self.driver.find_element(By.XPATH,"//button[contains(@class,'pass_show_hide')]")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", eye_button)
        self.driver.execute_script("arguments[0].click()",eye_button)
        time.sleep(2)
        pwd_field = pwd_input.get_attribute("type")
        print(pwd_field)
        return pwd_field