    
from PageObjects.CheckoutPage import CheckoutPage
from PageObjects.LoginPage import LoginPage
from PageObjects.BasePage import BasePage
from PageObjects.HomePage import HomePage
from PageObjects.CartPage import CartPage
from utils.logger_decorator import automation_logger


# class Tests:
#     @automation_logger
#     def test_correct_product_and_price_in_checkout_from_cart(self, change_language_and_verify1):
#         driver = change_language_and_verify1
#         home_page = HomePage(driver)
#         login_page = home_page.open_login_page()
#         login_page.select_email_login_option()
#         login_page.login_with_email_and_password("ashruti1@yopmail.com", "Test@1234")
#         home_page = HomePage(driver)
#         cart_page = home_page.open_cart_page()
#         cart_page = CartPage(driver)
#         cart_page.get_all_products_from_cart()
#         cart_page.checkout_on_cart_page()
#         checkoutpage = CheckoutPage(driver)
#         print("Items in Cart:", cart_page.items_in_cart)
#         for product in cart_page.items_in_cart:
#             checkoutpage.get_matching_product_name(product["name"])
#             checkoutpage.get_matching_product_price(product["price"])
#             assert True

#     def test_clicking_back_after_products_are_added_to_cart(self,change_language_and_verify1):
#         driver = change_language_and_verify1
#         home_page = HomePage(driver)
#         login_page = home_page.open_login_page()
#         login_page.select_email_login_option()
#         login_page.login_with_email_and_password("ashruti1@yopmail.com", "Test@1234")
#         home_page = HomePage(driver)
#         cart_page = home_page.open_cart_page()
#         cart_page = CartPage(driver)
#         products = cart_page.get_all_products_from_cart()
#         cart_page.checkout_on_cart_page()
#         driver.back()
#         after_back_products = cart_page.get_all_products_from_cart()
#         assert products == after_back_products

    