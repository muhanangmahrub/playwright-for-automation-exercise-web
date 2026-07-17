from playwright.sync_api import Page


class ProductDetailPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.wait_for_load_state("load")

    def increase_quantity(self, quantity: int):
        self.page.locator("#quantity").fill(str(quantity))

    def add_to_cart(self):
        self.page.get_by_role("button", name="Add to cart").click()

    def view_cart(self):
        self.page.get_by_role("link", name="View Cart").click()
