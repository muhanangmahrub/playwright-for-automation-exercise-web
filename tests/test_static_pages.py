from playwright.sync_api import expect

def test_verify_test_cases_page(page):
    page.goto("/")
    expect(page).to_have_title("Automation Exercise")

    page.locator(".shop-menu").get_by_role("link", name="Test Cases").click()
    expect(page).to_have_url("/test_cases")
    expect(page.get_by_text('Below is the list of test Cases for you to practice the Automation')).to_be_visible()