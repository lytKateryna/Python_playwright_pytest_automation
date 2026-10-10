from pages.base_page import BasePage


class Product(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.product_cart = page.locator(".single-products")
        self.add_to_cart_button = page.locator(".overlay-content:visible .btn")

        self.continue_shopping = page.get_by_role("button", name="Continue Shopping")

        self.view_cart = page.get_by_role("link", name="View Cart")

    def add_product_to_cart(self, product_index=0):
        self.product_cart.nth(product_index).hover()
        self.add_to_cart_button.nth(product_index).click()

    def button_continue_shopping(self):
        self.continue_shopping.click()

    def link_view_cart(self):
        self.view_cart.click()
