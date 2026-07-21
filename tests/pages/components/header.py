from playwright.sync_api import Page
from tests.pages.login_signup_page import LoginSignupPage
from tests.pages.delete_account_page import DeleteAccountPage
from tests.pages.products_page import ProductsPage
from tests.pages.contact_us_page import ContactUsPage
from tests.pages.cart_page import CartPage


class Header:
    def __init__(self, page: Page):
        self.page = page

    def go_to_login_signup_page(self):
        self.page.get_by_role("link", name="Signup / Login").click()
        return LoginSignupPage(self.page)

    def logout(self):
        self.page.get_by_role("link", name="Logout").click()

    def delete_account(self):
        self.page.get_by_role("link", name="Delete Account").click()
        return DeleteAccountPage(self.page)

    def go_to_products_page(self):
        self.page.locator(".shop-menu").get_by_role("link", name="Products").click()
        return ProductsPage(self.page)

    def go_to_contact_us_page(self):
        self.page.locator(".shop-menu").get_by_role("link", name="Contact us").click()
        return ContactUsPage(self.page)

    def go_back_home(self):
        self.page.locator("#form-section").get_by_role("link", name="Home").click()

    def go_to_cart_page(self):
        self.page.locator(".shop-menu").get_by_role("link", name="Cart").click()
        return CartPage(self.page)

    def is_logged_in(self):
        return self.page.get_by_role("link", name="Logout").is_visible()
