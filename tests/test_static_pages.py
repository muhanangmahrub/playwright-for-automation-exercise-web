from playwright.sync_api import expect, Page


def test_verify_test_cases_page(page: Page):
    # open the homepage and navigate to the test cases page
    page.goto("/")
    expect(page).to_have_title("Automation Exercise")
    page.locator(".shop-menu").get_by_role("link", name="Test Cases").click()
    expect(page).to_have_url("/test_cases")

    # assert that the test cases page is visible successfully
    test_cases_text = page.get_by_text(
        "Below is the list of test Cases for you to practice the Automation"
    )
    expect(test_cases_text).to_be_visible()
