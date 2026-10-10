def test_abrir_google(page):
    page.goto('https://www.google.com')
    page.get_by_role("link", name="Anmelden").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Google-Konto-Hilfe öffnen (").click()
    assert "Google" in page.title()