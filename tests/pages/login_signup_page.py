from playwright.sync_api import Page
from tests.pages.signup_detail_page import SignupDetailPage


class LoginSignupPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.wait_for_load_state("load")

    def login(self, email: str, password: str):
        self.page.locator("form").filter(has_text="Login").get_by_placeholder(
            "Email Address"
        ).fill(email)
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def signup(self, name: str, email: str):
        self.page.get_by_role("textbox", name="Name").fill(name)
        self.page.locator("form").filter(has_text="Signup").get_by_placeholder(
            "Email Address"
        ).fill(email)
        self.page.get_by_role("button", name="Signup").click()
        return SignupDetailPage(self.page)
