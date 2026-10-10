from pages.product import Product
from pages.cart import Cart


def test_product(page):
    product = Product(page)
    cart = Cart(page)
    product.go_to_home()
    product.close_ads()
    product.close_banner()
    product.product_cart.nth(0).hover()
    product.add_to_cart_button.nth(0).click()
    product.continue_shopping.click()
    product.product_cart.nth(1).hover()
    product.add_to_cart_button.nth(1).click()
    product.view_cart.click()
    cart.validate_cart(0, 'Blue Top', 'Women > Tops', 'Rs. 500', 'Rs. 500')
    cart.validate_cart(1, '	Men Tshirt', 'Men > Tshirts', 'Rs. 400', 'Rs. 400')
