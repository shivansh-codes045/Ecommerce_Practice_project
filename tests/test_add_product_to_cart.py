from PageObjects.LoginPage import LoginPage
from PageObjects.BasePage import BasePage
from PageObjects.HomePage import HomePage
from utils.logger_decorator import automation_logger


# class Tests:
#     @automation_logger
#     def test_adding_product_to_cart(self, change_language_and_verify1):
#         driver = change_language_and_verify1
#         home_page = HomePage(driver)
#         login_page = home_page.open_login_page()
#         login_page.select_email_login_option()
#         login_page.login_with_email_and_password("shivansh12@yopmail.com", "Shivansh@1234testing")
#         product = HomePage(driver)
#         product.from_all_products_select_n_number_of_products(2)
        
#     @automation_logger
#     def test_correct_product_and_price_in_cart_from_home_page(self, change_language_and_verify1):
#         driver = change_language_and_verify1
#         home_page = HomePage(driver)
#         cart_page = home_page.open_cart_page()
#         for product in home_page.all_products_added_to_cart:
#             cart_page.get_matching_product_name(product["name"])
#             cart_page.get_matching_product_price(product["price"])
#             assert True

    
