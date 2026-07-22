from playwright.sync_api import Page
from tests.pages.login_signup_page import LoginSignupPage
from tests.pages.delete_account_page import DeleteAccountPage
from tests.pages.products_page import ProductsPage
from tests.pages.contact_us_page import ContactUsPage
from tests.pages.cart_page import CartPage
from tests.pages.testcases_page import TestCasesPage


class Header:
    def __init__(self, page: Page):
        self.page = page
        self.logged_in_message = page.get_by_text("Logged in")
        self.logout_link = page.get_by_role("link", name="Logout")
        self.signup_login_link = page.get_by_role("link", name="Signup / Login")
        self.delete_account_link = page.get_by_role("link", name="Delete Account")
        self.products_link = page.locator(".shop-menu").get_by_role(
            "link", name="Products"
        )
        self.contact_us_link = page.locator(".shop-menu").get_by_role(
            "link", name="Contact us"
        )
        self.home_link = page.locator("#form-section").get_by_role("link", name="Home")
        self.cart_link = page.locator(".shop-menu").get_by_role("link", name="Cart")
        self.test_cases_link = page.locator(".shop-menu").get_by_role(
            "link", name="Test Cases"
        )

    def go_to_login_signup_page(self):
        self.signup_login_link.click()
        return LoginSignupPage(self.page)

    def logout(self):
        self.logout_link.click()

    def delete_account(self):
        self.delete_account_link.click()
        return DeleteAccountPage(self.page)

    def go_to_products_page(self):
        self.products_link.click()
        return ProductsPage(self.page)

    def go_to_contact_us_page(self):
        self.contact_us_link.click()
        return ContactUsPage(self.page)

    def go_back_home(self):
        self.home_link.click()

    def go_to_cart_page(self):
        self.cart_link.click()
        return CartPage(self.page)

    def go_to_test_cases_page(self):
        self.test_cases_link.click()
        return TestCasesPage(self.page)

    def is_logged_in(self):
        return self.logout_link.is_visible()
