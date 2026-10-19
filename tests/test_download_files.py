import os

def test_download_files(page):
    page.goto('https://www.transfernow.net/dl/20261017Ir8JGmde')
    page.get_by_role("button", name="Autoriser").click()
    with page.expect_download() as download_info:
        page.get_by_role("link", name="Alles herunterladen").click()

    download = download_info.value
    path = fr"C:\Users\megas\Python_playwright_pytest_automation\stores\test_file_upload\{download.suggested_filename}"
    download.save_as(path)

    assert os.path.exists(path), "Download file not found"
