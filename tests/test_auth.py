from playwright.sync_api import expect, Page


def test_register_user(page: Page, home, dummy_email, user_data):
    # open the homepage and navigate to the signup page
    login_signup_page = home.header.go_to_login_signup_page()

    # fill out the signup form and submit it
    signup_detail_page = login_signup_page.signup(user_data["name"], dummy_email)

    # assert that signup details page is visible
    expect(page.get_by_text("Enter Account Information")).to_be_visible()

    # fill out the account information form and submit it
    signup_detail_page.fill_account_information(
        title="Mr",
        password="testing",
        day="11",
        month="7",
        year="2004",
        newsletter=True,
        offers=True,
    )

    # assert that account created page is visible
    expect(page.get_by_text("Account Created!")).to_be_visible()
    signup_detail_page.continue_after_account_creation()

    # assert that user is logged in successfully and delete the account
    expect(page.get_by_text("Logged in")).to_be_visible()
    delete_account_page = home.header.delete_account()
    expect(page.get_by_text("Account Deleted!")).to_be_visible()
    delete_account_page.continue_after_account_deletion()


def test_login_user_with_correct_email_and_password(page: Page, home, credentials):
    # open the homepage and navigate to the login page
    login_signup_page = home.header.go_to_login_signup_page()

    # fill out the login form and submit it
    login_signup_page.login(credentials["email"], credentials["password"])

    # assert that user is logged in successfully
    expect(page.get_by_text("Logged in as")).to_be_visible()
    expect(page.get_by_role("link", name="Logout")).to_be_visible()


def test_login_user_with_incorrect_email_and_password(page: Page, home):
    # open the homepage and navigate to the login page
    login_signup_page = home.header.go_to_login_signup_page()

    # fill out the login form and submit it
    login_signup_page.login("testingincorrect@gmail.com", "superuser")

    # assert that user is not logged in and an error message is displayed
    expect(page.get_by_text("Your email or password is")).to_be_visible()


def test_logout_user(page: Page, home, credentials):
    # open the homepage and navigate to the login page
    login_signup_page = home.header.go_to_login_signup_page()

    # fill out the login form and submit it
    login_signup_page.login(credentials["email"], credentials["password"])

    # assert that user is logged in successfully
    expect(page.get_by_text("Logged in as")).to_be_visible()
    expect(page.get_by_role("link", name="Logout")).to_be_visible()

    # click the logout button and assert that user is logged out successfully
    home.header.logout()
    expect(page.get_by_role("link", name="Signup / Login")).to_be_visible()


def test_register_user_with_existing_email(page: Page, home, credentials):
    # open the homepage and navigate to the signup page
    login_signup_page = home.header.go_to_login_signup_page()

    # fill out the signup form and submit it
    login_signup_page.signup(
        credentials["existing_name"], credentials["existing_email"]
    )

    # assert that an error message is displayed for existing email
    expect(page.get_by_text("Email Address already exist!")).to_be_visible()
