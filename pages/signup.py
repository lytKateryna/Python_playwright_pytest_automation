from pages.base_page import BasePage


class Signup(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.input_email_signup = page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address")
        self.input_name_signup = page.get_by_role("textbox", name="Name")
        self.button_signup = page.get_by_role("button", name="Signup")
        # Signup Information
        self.checkbox_mr = page.get_by_role("radio", name="Mr.")
        self.checkbox_mrs = page.get_by_role("radio", name="Mrs.")
        self.input_password_signup = page.get_by_role("textbox", name="Password *")
        self.select_days = page.locator("#days")
        self.select_months = page.locator("#months")
        self.select_years = page.locator("#years")
        self.check_our_newsletter = page.get_by_role("checkbox", name="Sign up for our newsletter!")
        self.check_receive_special_offers = page.get_by_role("checkbox", name="Receive special offers from")
        self.input_first_name = page.get_by_role("textbox", name="First name *")
        self.input_last_name = page.get_by_role("textbox", name="Last name *")
        self.input_company = page.get_by_role("textbox", name="Company", exact=True)
        self.input_address = page.get_by_role("textbox", name="Address * (Street address, P.")
        self.input_address2 = page.get_by_role("textbox", name="Address 2")
        self.select_country = page.get_by_label("Country *")
        self.input_state = page.get_by_role("textbox", name="State *")
        self.input_city = page.get_by_role("textbox", name="City * Zipcode *")
        self.input_zipcode = page.locator("#zipcode")
        self.input_mobile_number = page.get_by_role("textbox", name="Mobile Number *")
        self.button_create_account = page.get_by_role("button", name="Create Account")
        self.button_continue = page.get_by_role("link", name="Continue")
        self.button_delete = page.get_by_role("link", name="Delete Account")

    def signup(self, name='', email=''):
        self.input_name_signup.fill(name)
        self.input_email_signup.fill(email)
        self.button_signup.click()

    def select_title(self, title):
        if title == 'Mr.':
            self.checkbox_mr.check()
        elif title == 'Mrs.':
            self.checkbox_mrs.check()

    def fill_account_information(
            self,
            password='',
            days='',
            months='',
            years='',
            check_our_newsletter: bool = False,
            check_receive_special_offers: bool = False):
        if password:
            self.input_password_signup.fill(password)
        if days:
            self.select_days.select_option(days)
        if months:
            self.select_months.select_option(months)
        if years:
            self.select_years.select_option(years)
        if check_our_newsletter:
            self.check_our_newsletter.check()
        else:
            self.check_our_newsletter.uncheck()
        if check_receive_special_offers:
            self.check_receive_special_offers.check()
        else:
            self.check_receive_special_offers.uncheck()

    def fill_address_information(
            self,
            first_name='',
            last_name='',
            company='',
            address='',
            address2='',
            country='',
            state='',
            city='',
            zipcode='',
            mobile_number=''):
        if first_name:
            self.input_first_name.fill(first_name)
        if last_name:
            self.input_last_name.fill(last_name)
        if company:
            self.input_company.fill(company)
        if address:
            self.input_address.fill(address)
        if address2:
            self.input_address2.fill(address2)
        if country:
            self.select_country.select_option(country)
        if state:
            self.input_state.fill(state)
        if city:
            self.input_city.fill(city)
        if zipcode:
            self.input_zipcode.fill(zipcode)
        if mobile_number:
            self.input_mobile_number.fill(mobile_number)

    def create_account(self):
        self.button_create_account.click()
