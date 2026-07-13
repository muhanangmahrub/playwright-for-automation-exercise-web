from playwright.sync_api import expect, Page


def test_register_user(page: Page):
    # open the homepage and navigate to the signup page
    page.goto("/")
    expect(page).to_have_title("Automation Exercise")
    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_role("heading", name="New User Signup!")).to_be_visible()

    # fill out the signup form and submit it
    page.get_by_role("textbox", name="Name").fill("Febri Haryono")
    page.locator("form").filter(has_text="Signup").get_by_placeholder(
        "Email Address"
    ).fill("febriharyono@gmail.com")
    page.get_by_role("button", name="Signup").click()

    # assert that signup details page is visible
    expect(page.get_by_text("Enter Account Information")).to_be_visible()

    # fill out the account information form and submit it
    page.get_by_role("radio", name="Mr.").check()
    page.get_by_role("textbox", name="Password *").fill("testing")
    page.locator("#days").select_option("11")
    page.locator("#months").select_option("7")
    page.locator("#years").select_option("2004")
    page.get_by_role("checkbox", name="Sign up for our newsletter!").check()
    page.get_by_role("checkbox", name="Receive special offers from").check()
    page.get_by_role("textbox", name="First name *").fill("Febri")
    page.get_by_role("textbox", name="Last name *").fill("Haryono")
    page.get_by_role("textbox", name="Company", exact=True).fill("Nawadata")
    page.get_by_role("textbox", name="Address * (Street address, P.").fill("Baciro")
    page.get_by_role("textbox", name="Address 2").fill("Gondokusuman")
    page.get_by_label("Country *").select_option("Australia")
    page.get_by_role("textbox", name="State *").fill("Oakland")
    page.get_by_role("textbox", name="City * Zipcode *").fill("Oklahoma")
    page.locator("#zipcode").fill("12345")
    page.get_by_role("textbox", name="Mobile Number *").fill("123456789")
    page.get_by_role("button", name="Create Account").click()

    # assert that account created page is visible
    expect(page.get_by_text("Account Created!")).to_be_visible()
    page.get_by_role("link", name="Continue").click()

    # assert that user is logged in successfully and delete the account
    expect(page.get_by_text("Logged in")).to_be_visible()
    page.get_by_role("link", name="Delete Account").click()
    expect(page.get_by_text("Account Deleted!")).to_be_visible()
    page.get_by_role("link", name="Continue").click()
