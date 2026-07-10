from playwright.sync_api import expect

def test_open_google(page):
    page.goto('https://www.google.com')
    expect(page).to_have_title("Google")