from playwright.sync_api import TimeoutError


class BasePage:
    def __init__(self, page):
        self.page = page
        self.home_link = page.get_by_role("link", name="Home")
        self.close_popup_link = page.get_by_role("button", name="Einwilligen")
        self.close_banner_link = page.locator(".grippy-host")
        self.products_link = page.get_by_role("link", name="Products")
        self.cart_link = page.get_by_role("link", name="Cart")
        self.signup_login_link = page.get_by_role("link", name="Signup / Login")
        self.signup_link = page.get_by_role("link", name="signup")
        self.close_ads_link = page.get_by_role("link", name="Close Ads")
        self.close_ad_button = page.locator("iframe[name=\"aswift_2\"]").content_frame.get_by_role("button",
                                                                                                   name="Close ad")
        self.werbung_vor_delete = page.locator("iframe[name=\"aswift_3\"]").content_frame.get_by_role("button",
                                                                                                      name="Close ad")
        self.logout_link = page.get_by_role("link", name="Logout")

    def go_to_home(self):
        self.page.goto('')

    def go_to_products(self):
        self.page.goto('products', wait_until="domcontentloaded")

    def go_to_cart(self):
        self.page.goto('cart')

    def go_to_signup_login(self):
        self.page.goto('login')

    def go_to_signup(self):
        self.page.goto('signup')

    def close_ads(self):
        try:
            self.close_popup_link.wait_for(
                state="visible",
                timeout=5000
            )
            self.close_popup_link.click()
        except TimeoutError:
            pass

    def close_banner(self):
        if self.close_banner_link.is_visible():
            self.close_banner_link.click()

    def close_google_ads(self):
        if self.close_ad_button.is_visible():
            self.close_ad_button.click()

        if self.werbung_vor_delete.is_visible():
            self.werbung_vor_delete.click()

    def logout(self):
        self.logout_link.click()
