from playwright.sync_api import expect

def test_file_upload(page):
    page.goto('https://transfernow.net/')
    page.get_by_role("button", name="OK für mich").click()
    with page.expect_file_chooser() as fc_info:
        page.get_by_role("button", name="Start").click()
        file_chooser = fc_info.value
        file_chooser.set_files(r"C:\Users\megas\Python_playwright_pytest_automation\stores\test_file_upload\teste123.txt")
        page.get_by_role("button", name="Link erstellen").click()
        page.get_by_role("textbox", name="Ihre Emailadresse").fill("megaspektr.e@gmail.com")
        page.get_by_role("button", name="Link erhalten").click()
        expect(page.get_by_text("Ihr Link ist fertig!")).to_be_visible(timeout=30000)


def test_file_upload_multiple(page):
    page.goto('https://transfernow.net/')
    page.get_by_role("button", name="OK für mich").click()
    with page.expect_file_chooser() as fc_info:
        page.get_by_role("button", name="Start").click()
        file_chooser = fc_info.value
        file_chooser.set_files([r"C:\Users\megas\Python_playwright_pytest_automation\stores\test_file_upload\teste123.txt",
                                r"C:\Users\megas\Python_playwright_pytest_automation\stores\test_file_upload\teste456.txt"])
        page.get_by_role("button", name="Link erstellen").click()
        page.get_by_role("textbox", name="Ihre Emailadresse").fill("megaspektr.e@gmail.com")
        page.get_by_role("button", name="Link erhalten").click()
        expect(page.get_by_text("Ihr Link ist fertig!")).to_be_visible(timeout=30000)
        page.pause()