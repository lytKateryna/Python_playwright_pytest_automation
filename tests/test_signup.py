from pages.signup import Signup
from playwright.sync_api import expect

def test_signup_account_is_visible(page):
    signup = Signup(page)
    signup.go_to_signup_login()
    signup.close_ads()
    expect(page.get_by_text("New User Signup! Signup")).to_be_visible()


def test_create_signup_account(page):
    signup = Signup(page)
    signup.go_to_signup_login()
    signup.close_ads()
    signup.signup(name='Linda', email='megaspektr.e+2@gmail.com')
    expect(page.get_by_text("Enter Account Information")).to_be_visible()
    #next step
    signup.select_title('Mrs.')
    signup.fill_account_information(
        password="123456789",
        days='1',
        months='12',
        years='1988',
        check_our_newsletter=True,
        check_receive_special_offers=True
    )
    signup.fill_address_information(
        first_name='Linda',
        last_name='Doe',
        company='ITCH',
        address='Berlin',
        address2='Hanover',
        country='India',
        state='Berlin',
        city='Berlin',
        zipcode='12345',
        mobile_number='+49123456789'
    )
    signup.create_account()
    expect(page.get_by_text("Account Created!")).to_be_visible()
    page.get_by_role("link", name="Continue").click()
    signup.close_google_ads()
    expect(page.get_by_text("Logged in as Linda")).to_be_visible()
    signup.close_google_ads()
    signup.button_delete.click()
    signup.close_google_ads()
    expect(page.get_by_text("Account Deleted!")).to_be_visible()



