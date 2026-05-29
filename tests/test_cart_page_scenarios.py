from PageObjects.LoginPage import LoginPage
from PageObjects.BasePage import BasePage
from PageObjects.HomePage import HomePage
from PageObjects.CartPage import CartPage
from utils.logger_decorator import automation_logger


# class Tests:
#     @automation_logger
#     def test_increasing_product_quantity_in_cart(self, change_language_and_verify1):
#         driver = change_language_and_verify1
#         home_page = HomePage(driver)
#         cart_page = home_page.open_cart_page()
#         quantity_before = cart_page.get_product_quantity_in_cart("Dark Brown Wooden Dining Table with 6 Chairs Set")

#     @automation_logger
#     def test_total_price_of_items_matches_with_bill_price(self, change_language_and_verify1):
#         driver = change_language_and_verify1
#         home_page = HomePage(driver)
#         login_page = home_page.open_login_page()
#         login_page.select_email_login_option()
#         login_page.login_with_email_and_password("shivansh12@yopmail.com", "Shivansh@1234testing")
#         home_page = HomePage(driver)
#         cart_page = home_page.open_cart_page()
#         cart_page = CartPage(driver)
#         total_price_of_items = cart_page.get_total_item_price_in_cart()
#         total_price_in_bill = cart_page.get_total_price_in_bill()
#         print("Total Price of Items in Cart:", total_price_of_items)
#         print("Total Price in Bill:", total_price_in_bill)
#         assert total_price_of_items == total_price_in_bill

#     @automation_logger
#     def test_increasing_product_quantity_in_cart(self, change_language_and_verify1):
#         driver = change_language_and_verify1
#         home_page = HomePage(driver)
#         login_page = home_page.open_login_page()
#         login_page.select_email_login_option()
#         login_page.login_with_email_and_password("shivansh12@yopmail.com", "Shivansh@1234testing")
#         home_page = HomePage(driver)
#         cart_page = home_page.open_cart_page()
#         cart_page = CartPage(driver)
#         values = cart_page.increase_product_quantity_in_cart("Dark Brown Wooden Dining Table with 6 Chairs Set")
#         assert values["after"] == values["before"] + 1

#     @automation_logger
#     def test_decreasing_product_quantity_in_cart_where_quantity_is_equal_to_one(self, change_language_and_verify1):
#         driver = change_language_and_verify1
#         home_page = HomePage(driver)
#         login_page = home_page.open_login_page()
#         login_page.select_email_login_option()
#         login_page.login_with_email_and_password("ashruti1@yopmail.com", "Test@1234")
#         home_page = HomePage(driver)
#         cart_page = home_page.open_cart_page()
#         cart_page = CartPage(driver)
#         values = cart_page.decrease_product_quantity_in_cart_where_quantity_is_equal_to_one("Modern L-Shaped Sofa in Light Gray")
#         print("values before =",values["before"],"values after =",values["after"])
#         assert values["after"] == values["before"]

#     @automation_logger
#     def test_decreasing_product_quantity_in_cart_where_quantity_is_greater_than_one(self, change_language_and_verify1):
#         driver = change_language_and_verify1
#         home_page = HomePage(driver)
#         login_page = home_page.open_login_page()
#         login_page.select_email_login_option()
#         login_page.login_with_email_and_password("shivansh12@yopmail.com", "Shivansh@1234testing")
#         home_page = HomePage(driver)
#         cart_page = home_page.open_cart_page()
#         cart_page = CartPage(driver)
#         values = cart_page.decrease_product_quantity_in_cart_where_quantity_is_greater_than_one("Dark Brown Wooden Dining Table with 6 Chairs Set")
#         assert values["after"] == values["before"] - 1

#     @automation_logger
#     def test_removing_product_from_cart(self, change_language_and_verify1):
#         driver = change_language_and_verify1
#         home_page = HomePage(driver)
#         login_page = home_page.open_login_page()
#         login_page.select_email_login_option()
#         login_page.login_with_email_and_password("ashruti1@yopmail.com", "Test@1234")
#         home_page = HomePage(driver)
#         cart_page = home_page.open_cart_page()
#         cart_page = CartPage(driver)
#         products = cart_page.remove_product_from_cart("Comfortable 3 Seater Sofa")
#         assert products["after"] == products["before"] - 1

#     @automation_logger
#     def test_empty_cart(self, change_language_and_verify1):
#         driver = change_language_and_verify1
#         home_page = HomePage(driver)
#         login_page = home_page.open_login_page()
#         login_page.select_email_login_option()
#         login_page.login_with_email_and_password("ashruti1@yopmail.com", "Test@1234")
#         home_page = HomePage(driver)
#         cart_page = home_page.open_cart_page()
#         cart_page = CartPage(driver)
#         cart_page.empty_cart()
    
#     @automation_logger
#     def test_checking_out_on_empty_cart(self,change_language_and_verify1):
#         driver = change_language_and_verify1
#         home_page = HomePage(driver)
#         login_page = home_page.open_login_page()
#         login_page.select_email_login_option()
#         login_page.login_with_email_and_password("ashruti1@yopmail.com", "Test@1234")
#         home_page = HomePage(driver)
#         cart_page = home_page.open_cart_page()
#         cart_page = CartPage(driver)
#         cart_page = cart_page.is_checkout_button_present()
#         assert cart_page == False

#     @automation_logger
#     def test_checking_items_present_in_cart(self,change_language_and_verify1):
#         driver = change_language_and_verify1
#         home_page = HomePage(driver)
#         login_page = home_page.open_login_page()
#         login_page.select_email_login_option()
#         login_page.login_with_email_and_password("ashruti1@yopmail.com", "Test@1234")
#         home_page = HomePage(driver)
#         cart_page = home_page.open_cart_page()
#         cart_page = CartPage(driver)
#         products = cart_page.get_all_products_from_cart()
#         print(products)

