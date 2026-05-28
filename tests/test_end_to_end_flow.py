from PageObjects.LoginPage import LoginPage
from PageObjects.BasePage import BasePage
from PageObjects.HomePage import HomePage
from PageObjects.CartPage import CartPage
from PageObjects.CheckoutPage import CheckoutPage
from tests.test_add_product_to_cart import Tests
from utils.logger_decorator import automation_logger

class Tests:
    def test_adding_products_from_cart_validating_product_details_in_cart_and_checking_out_products(self,change_language_and_verify1):
        driver = change_language_and_verify1
        home_page = HomePage(driver)
        login_page = home_page.open_login_page()
        login_page.select_email_login_option()
        login_page.login_with_email_and_password("ashruti1@yopmail.com", "Test@1234")
        product = HomePage(driver)
        product.from_all_products_select_n_number_of_products(2)
        cart_page = home_page.open_cart_page()
        cart_page = CartPage(driver)
        cart_products = cart_page.get_all_products_from_cart()
        cart_page.checkout_on_cart_page()
        checkoutpage = CheckoutPage(driver)
        checkout_products = checkoutpage.get_all_products_from_checkout()
        print("Items in Cart:", cart_products)
        print("Items in checkout:", checkout_products)
        assert cart_products == checkout_products