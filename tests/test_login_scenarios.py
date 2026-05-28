import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.BasePage import BasePage
from PageObjects.HomePage import HomePage   
from utils.logger_decorator import automation_logger

class Tests:

    @automation_logger
    def test_login_with_valid_credentials(self, change_language_and_verify):
        driver = change_language_and_verify
        home_page = HomePage(driver)
        login_page = home_page.open_login_page()
        login_page.select_email_login_option()
        login_page.login_with_email_and_password("shivansh12@yopmail.com", "Shivansh@1234testing")
        home_page.verify_user_logged_in()

    @automation_logger
    @pytest.mark.parametrize("email,password", [("test", "wrongpassword"), ("test1@", "password123"),("test1@yop", "password123"), ("@yopmail.com", "password123"),("", "password123")])
    def test_login_with_invalid_email_format(self, change_language_and_verify, email, password):
        driver = change_language_and_verify
        home_page = HomePage(driver)
        login_page = home_page.open_login_page()
        login_page.select_email_login_option()
        login_page.login_with_email_and_password(email, password)
        print("Error Message Displayed:", login_page.get_error_message())
        assert login_page.get_error_message() in "Please enter valid email address."

    @automation_logger
    def test_login_with_incorrect_password(self,change_language_and_verify):
        driver = change_language_and_verify
        home_page = HomePage(driver)
        login_page = home_page.open_login_page()
        login_page.select_email_login_option()
        login_page.login_with_email_and_password("shivansh12@yopmail.com", "Shivansh@123testing")
        print("Error Message Displayed:", login_page.get_error_message())
        assert login_page.get_error_message() in "You have entered incorrect email or password."
    
    @automation_logger
    def test_user_input_password_is_masked(self,change_language_and_verify1):
        driver = change_language_and_verify1
        home_page = HomePage(driver)
        login_page = home_page.open_login_page()
        login_page.select_email_login_option()
        pwd_field = login_page.check_password_field()       
        assert pwd_field == "password"

    @automation_logger
    def test_after_user_clicks_eye_button_password_is_shown(self,change_language_and_verify1):
        driver = change_language_and_verify1
        home_page = HomePage(driver)
        login_page = home_page.open_login_page()
        login_page.select_email_login_option()
        type_of_pwd = login_page.click_password_eye_button_after_entering_password("pwd")
        assert type_of_pwd == "text"