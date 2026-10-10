from pages.signup_login import SignupLogin
from playwright.sync_api import expect

def test_login_invalid(page):
    login = SignupLogin(page)
    login.go_to_signup_login()
    login.close_ads()
    login.login(email='myt.kateryna@gmail.com', password='1234567')
    expect(page.get_by_text("Your email or password is")).to_be_visible()

def teste_login_email(page):
    login = SignupLogin(page)
    login.go_to_signup_login()
    login.close_ads()
    login.login(email='lyt.kateryna+1@gmail.com', password='123456789')
    expect(page.get_by_role("link", name="Logout")).to_be_visible()
    expect(page.get_by_text("Logged in as Kate")).to_be_visible()


def teste_logout(page):
    login = SignupLogin(page)
    login.go_to_signup_login()
    login.close_ads()
    login.login(email='lyt.kateryna+1@gmail.com', password='123456789')
    login.go_to_home()
    login.close_ads()
    expect(page.get_by_role("link", name="Logout")).to_be_visible()
    login.logout()
    expect(page.get_by_role("link", name="Signup / Login")).to_be_visible()

def test_user_not_logged_in(page):
    login = SignupLogin(page)
    login.go_to_home()
    login.close_ads()
    expect(page.get_by_role("link", name="Logout")).not_to_be_visible()


