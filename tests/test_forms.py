from playwright.sync_api import expect, Page
from pathlib import Path


def test_contact_us_form(page: Page):
    page.on("dialog", lambda dialog: dialog.accept())

    # open the homepage and navigate to the contact us page
    page.goto("/")
    expect(page).to_have_title("Automation Exercise")

    page.locator(".shop-menu").get_by_role("link", name="Contact us").click()
    page.wait_for_load_state("load")
    expect(page).to_have_url("/contact_us")
    expect(page.get_by_text("GET IN TOUCH")).to_be_visible()

    # fill out the contact us form and submit it
    page.get_by_placeholder("Name").fill("Peter")
    page.get_by_placeholder("Email", exact=True).fill("peterpan@gmail.com")
    page.get_by_placeholder("Subject").fill("Account Locked")
    page.get_by_placeholder("Your Message Here").fill(
        "My account got locked out and I need help unlocking it."
    )

    # upload a file
    file_path = Path(__file__).parent / "file_test.pdf"
    page.locator('input[type="file"]').set_input_files(file_path)

    page.locator("input[data-qa='submit-button']").click()

    # assert that the success message is visible
    expect(
        page.locator("#contact-page").get_by_text(
            "Success! Your details have been submitted successfully."
        )
    ).to_be_visible()

    # navigate back to the home page
    page.locator("#form-section").get_by_role("link", name="Home").click()
    expect(page).to_have_url("/")
    expect(page.get_by_role("heading", name="AutomationExercise").first).to_be_visible()


def test_verify_subscription_in_home_page(page: Page):
    # open the homepage
    page.goto("/")
    expect(page).to_have_title("Automation Exercise")

    # scroll to the footer and subscribe to the newsletter
    page.locator("#footer").scroll_into_view_if_needed()
    expect(page.get_by_role("heading", name="Subscription")).to_be_visible()
    email_dummy = "test@example.com"
    page.get_by_role("textbox", name="Your email address").fill(email_dummy)
    page.locator("#subscribe").click()
    expect(page.get_by_text("You have been successfully")).to_be_visible()


def test_verify_subscription_in_cart_page(page: Page):
    # open the homepage and navigate to the cart page
    page.goto("/")
    expect(page).to_have_title("Automation Exercise")
    page.get_by_role("link", name="Products").click()
    expect(page).to_have_url("/products")

    # scroll to the footer and subscribe to the newsletter
    page.locator("#footer").scroll_into_view_if_needed()
    expect(page.get_by_role("heading", name="Subscription")).to_be_visible()
    email_dummy = "test@example.com"
    page.get_by_role("textbox", name="Your email address").fill(email_dummy)
    page.locator("#subscribe").click()
    expect(page.get_by_text("You have been successfully")).to_be_visible()
