from playwright.sync_api import expect


def test_click(page):
    page.goto('https://automationexercise.com/')
    page.pause()
    page.get_by_role("link", name="Website for automation").click(position={'x': 50, 'y': 70})
    page.get_by_role("link", name="(5) H&M").click()
    page.get_by_role("link", name="(5) H&M").click(modifiers=["Control"])


def test_click(page):
    page.goto('https://bootswatch.com/default/')
    page.pause()
    # page.get_by_role('button', name='Primary').nth(1).click(force=True)
    page.get_by_role('button', name='Primary').nth(1).click(timeout=5000)


def test_fill(page):
    page.goto('https://automationexercise.com/login')
    page.get_by_role("button", name="Einwilligen").click()
    page.pause()
    page.get_by_role("textbox", name="Name").fill('Jeferson')
    page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").fill('jeferson@gmail.com')
    page.get_by_role("button", name="Signup").click()


def test_check_uncheck(page):
    page.goto('https://bootswatch.com/default/')
    page.pause()
    page.get_by_role("checkbox", name="Default checkbox").check()
    page.get_by_role("checkbox", name="Checked checkbox").uncheck()


def test_select_option(page):
    page.goto('https://bootswatch.com/default/')
    page.pause()
    page.get_by_label("Example multiple select").select_option("2")
    page.get_by_label("Example select").select_option("5")


def test_press(page):
    page.goto('https://bootswatch.com/default/')
    page.pause()
    page.get_by_placeholder("name@example.com").fill("teste@gmail.com")
    page.locator("#floatingPassword").fill("123456789")
    page.get_by_placeholder("name@example.com").press("Tab")
    page.keyboard.type("1234")


def test_hover(page):
    page.goto('https://automationexercise.com/')
    page.get_by_role("button", name="Einwilligen").click()
    page.locator(".grippy-host").click()
    page.pause()
    product = page.locator(
        ".single-products:visible"
    ).filter(has_text="Blue Top").first

    product.hover()

    product.locator(
        ".product-overlay .add-to-cart"
    ).dispatch_event("click")


def test_expect(page):
    page.goto('https://automationexercise.com/')
    page.get_by_role("button", name="Einwilligen").click()
    page.locator(".grippy-host").click()
    page.pause()
    page.locator(
        ".single-products:visible"
    ).filter(has_text="Blue Top").first.hover()

    page.get_by_text("Add to cart").nth(1).click()
    expect(page.locator('#cartModal')).to_contain_text('Your product has been added to cart.', timeout=10000)
    expect(page.get_by_role('button', name='Continue Shopping')).to_be_visible()
    expect(page.get_by_role('button', name='Continue Shopping')).to_be_enabled()
    page.get_by_role('button', name='Continue Shopping').click()
    expect(page.locator('#cartModal')).not_to_be_visible()
