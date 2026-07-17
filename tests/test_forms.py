from playwright.sync_api import expect, Page
from pathlib import Path


def test_contact_us_form(page: Page, home):
    page.on("dialog", lambda dialog: dialog.accept())
    contact_us_page = home.header.go_to_contact_us_page()
    expect(page).to_have_url("/contact_us")
    expect(page.get_by_text("GET IN TOUCH")).to_be_visible()

    # fill out the contact us form and submit it
    file_path = Path(__file__).parent / "file_test.pdf"
    contact_us_page.fill_customer_information(
        "Peter",
        "peterpan@gmail.com",
        "Account Locked",
        "My account got locked out and I need help unlocking it.",
        file_path,
    )
    contact_us_page.click_submit()

    # assert that the success message is visible
    expect(
        page.locator("#contact-page").get_by_text(
            "Success! Your details have been submitted successfully."
        )
    ).to_be_visible()

    # navigate back to the home page
    home.header.go_back_home()
    expect(page).to_have_url("/")
    expect(page.get_by_role("heading", name="AutomationExercise").first).to_be_visible()


def test_verify_subscription_in_home_page(page: Page, home):
    # scroll to the footer and subscribe to the newsletter
    home.footer.scroll_to_footer()
    expect(page.get_by_role("heading", name="Subscription")).to_be_visible()
    home.footer.subscribe("emailtest@gmail.com")
    expect(page.get_by_text("You have been successfully")).to_be_visible()


def test_verify_subscription_in_cart_page(page: Page, home):
    # open the homepage and navigate to the cart page
    home.header.go_to_cart_page()
    expect(page).to_have_url("/view_cart")

    # scroll to the footer and subscribe to the newsletter
    home.footer.scroll_to_footer()
    expect(page.get_by_role("heading", name="Subscription")).to_be_visible()
    home.footer.subscribe("emailtest@gmail.com")
    expect(page.get_by_text("You have been successfully")).to_be_visible()
