from pages.base_page import BasePage
from playwright.sync_api import expect

class Cart(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.product_description_header = page.locator('.cart_description h4')
        self.product_description = page.locator('.cart_description p')
        self.product_price = page.locator('.cart_price')
        self.product_total_price = page.locator('.cart_total_price')


    def validate_cart(self, product_index, product_name, product_description, product_price, product_total_price):
        expect(self.product_description_header.nth(product_index)).to_have_text(product_name)
        expect(self.product_description.nth(product_index)).to_have_text(product_description)
        expect(self.product_price.nth(product_index)).to_have_text(product_price)
        expect(self.product_total_price.nth(product_index)).to_have_text(product_total_price)