from playwright.sync_api import Page
from tests.pages.login_signup_page import LoginSignupPage
from tests.pages.address_page import AddressPage


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.wait_for_load_state("load")

    def proceed_to_checkout_as_guest(self):
        self.page.get_by_text("Proceed To Checkout").click()

    def proceed_to_checkout(self):
        self.page.get_by_text("Proceed To Checkout").click()
        return AddressPage(self.page)

    def register_or_login(self):
        self.page.locator(".modal-content").get_by_role(
            "link", name="Register / Login"
        ).click()
        return LoginSignupPage(self.page)

    def remove_product(self, product_id: int):
        self.page.locator(
            f"#product-{product_id + 1} > .cart_delete > .cart_quantity_delete"
        ).click()
