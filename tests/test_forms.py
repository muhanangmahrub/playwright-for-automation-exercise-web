from playwright.sync_api import expect
from pathlib import Path

def test_contact_us_form(page):
    page.goto("/")
    expect(page).to_have_title("Automation Exercise")

    page.locator(".shop-menu").get_by_role("link", name="Contact us").click()
    page.wait_for_load_state("load")
    expect(page).to_have_url("/contact_us")
    expect(page.get_by_text('GET IN TOUCH')).to_be_visible()

    page.get_by_placeholder('Name').fill('Peter')
    page.get_by_placeholder('Email', exact=True).fill('peterpan@gmail.com')
    page.get_by_placeholder('Subject').fill('Account Locked')
    page.get_by_placeholder('Your Message Here').fill('I have an account that cant locked out.')

    file_path = Path(__file__).parent / "file_test.pdf"
    page.locator('input[type="file"]').set_input_files(file_path)

    page.on("dialog", lambda dialog: dialog.accept())
    page.locator("input[data-qa='submit-button']").click()

    expect(page.locator("#contact-page").get_by_text('Success! Your details have been submitted successfully.')).to_be_visible()

    page.locator("#form-section").get_by_role("link", name="Home").click()
    expect(page).to_have_url("/")
    expect(page.get_by_role("heading", name="AutomationExercise").first).to_be_visible()