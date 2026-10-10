from pages.base_page import BasePage

class SignupLogin(BasePage):
    def __init__(self, page):
        super().__init__(page)
        #Login
        self.input_email_login = page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address")
        self.input_password_login = page.get_by_role("textbox", name="Password")
        self.button_login = page.get_by_role("button", name="Login")


    def login(self, email='', password=''):
        self.input_email_login.fill(email)
        self.input_password_login.fill(password)
        self.button_login.click()








