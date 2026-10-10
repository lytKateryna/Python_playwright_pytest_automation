import pytest

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context(base_url='https://automationexercise.com/',
                                  record_video_dir= 'videos')
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    page.set_default_timeout(10000)
    page.set_default_navigation_timeout(30000)
    yield page
    page.close()