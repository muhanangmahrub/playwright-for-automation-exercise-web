from playwright.sync_api import Page
from tests.pages.cart_page import CartPage


class ProductDetailPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.wait_for_load_state("load")
        self.product_information = page.locator(".product-information")
        self.availability_label = self.product_information.get_by_text("Availability:")
        self.condition_label = self.product_information.get_by_text("Condition:")
        self.brand_label = self.product_information.get_by_text("Brand:")
        self.quantity_textbox = page.locator("#quantity")
        self.add_to_cart_button = page.get_by_role("button", name="Add to cart")
        self.view_cart_link = page.get_by_role("link", name="View Cart")

    def increase_quantity(self, quantity: int):
        self.quantity_textbox.fill(str(quantity))

    def add_to_cart(self):
        self.add_to_cart_button.click()

    def view_cart(self):
        self.view_cart_link.click()
        return CartPage(self.page)
