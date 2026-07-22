from playwright.sync_api import Page
from tests.pages.signup_detail_page import SignupDetailPage


class LoginSignupPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.wait_for_load_state("load")
        self.invalid_credentials_error = page.get_by_text("Your email or password is")
        self.email_already_exists_error = page.get_by_text(
            "Email Address already exist!"
        )
        self.login_email_textbox = (
            page.locator("form")
            .filter(has_text="Login")
            .get_by_placeholder("Email Address")
        )
        self.password_textbox = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.name_textbox = page.get_by_role("textbox", name="Name")
        self.signup_email_textbox = (
            page.locator("form")
            .filter(has_text="Signup")
            .get_by_placeholder("Email Address")
        )
        self.signup_button = page.get_by_role("button", name="Signup")

    def login(self, email: str, password: str):
        self.login_email_textbox.fill(email)
        self.password_textbox.fill(password)
        self.login_button.click()

    def signup(self, name: str, email: str):
        self.name_textbox.fill(name)
        self.signup_email_textbox.fill(email)
        self.signup_button.click()
        return SignupDetailPage(self.page)
