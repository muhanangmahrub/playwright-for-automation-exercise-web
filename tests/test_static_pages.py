from playwright.sync_api import expect, Page


def test_verify_test_cases_page(page: Page, home):
    # open the homepage and navigate to the test cases page
    expect(page).to_have_title("Automation Exercise")
    test_cases_page = home.header.go_to_test_cases_page()
    expect(page).to_have_url("/test_cases")

    # assert that the test cases page is visible successfully
    expect(test_cases_page.description_message).to_be_visible()
