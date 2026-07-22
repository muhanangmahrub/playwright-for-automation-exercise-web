from playwright.sync_api import Page
from tests.pages.login_signup_page import LoginSignupPage
from tests.pages.address_page import AddressPage


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.wait_for_load_state("load")
        self.proceed_to_checkout_button = page.get_by_text("Proceed To Checkout")
        self.register_login_link = page.locator(".modal-content").get_by_role(
            "link", name="Register / Login"
        )

    def product_row(self, product_id: int):
        return self.page.locator(f"#product-{product_id + 1}")

    def product_name(self, product_id: int):
        return self.product_row(product_id).locator(".cart_description")

    def product_price(self, product_id: int):
        return self.product_row(product_id).locator(".cart_price")

    def product_quantity(self, product_id: int):
        return self.product_row(product_id).locator(".cart_quantity")

    def product_total(self, product_id: int):
        return self.product_row(product_id).locator(".cart_total")

    def proceed_to_checkout_as_guest(self):
        self.proceed_to_checkout_button.click()

    def proceed_to_checkout(self):
        self.proceed_to_checkout_button.click()
        return AddressPage(self.page)

    def register_or_login(self):
        self.register_login_link.click()
        return LoginSignupPage(self.page)

    def remove_product(self, product_id: int):
        self.product_row(product_id).locator(
            ".cart_delete > .cart_quantity_delete"
        ).click()
