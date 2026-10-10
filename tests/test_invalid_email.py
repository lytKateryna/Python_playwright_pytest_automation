from pages.signup_login import SignupLogin
from playwright.sync_api import expect

def test_invalid_email(page):
    login = SignupLogin(page)
    login.go_to_home()
    login.close_ads()
    expect(page.get_by_role("link", name="Home")).to_be_visible()
    login.go_to_signup_login()
    login.close_ads()
    expect(page.get_by_role("heading", name="Login to your account")).to_be_visible()
    login.login(email='lyt.kateryna@gmail.com', password='123456789')
    expect(page.get_by_text("Your email or password is incorrect!")).to_be_visible()

def test_positive_login(page):
    login = SignupLogin(page)
    login.go_to_home()
    login.close_ads()
    expect(page.get_by_role("link", name="Home")).to_be_visible()
    login.go_to_signup_login()
    login.close_ads()
    login.login(email='megaspektr.e@gmail.com', password='123456789')
    expect(page.get_by_text("Logged in as Test")).to_be_visible()