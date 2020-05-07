# Page of article in internet-shop
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        # TD - write some checks!
        pass

    def add_to_cart(self):
        self.click_on_element(*ProductPageLocators.BASKET_BTN)