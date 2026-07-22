from playwright.sync_api import Page
from tests.pages.cart_page import CartPage
from tests.pages.product_detail_page import ProductDetailPage


class ProductList:
    def __init__(self, page: Page):
        self.page = page
        self.product_cards = page.locator(".features_items .product-image-wrapper")
        self.continue_shopping_button = page.get_by_role(
            "button", name="Continue Shopping"
        )
        self.view_cart_link = page.get_by_role("link", name="View Cart")
        self.search_textbox = page.get_by_role("textbox", name="Search Product")
        self.search_button = page.locator("#submit_search")

    def continue_shopping(self):
        self.continue_shopping_button.click()

    def add_nth_product_to_cart(self, n: int):
        self.product_cards.nth(n).locator(".productinfo").get_by_text(
            "Add to cart"
        ).click()

    def view_cart(self):
        self.view_cart_link.click()
        return CartPage(self.page)

    def view_product_details_of_nth_product(self, n: int):
        self.page.wait_for_load_state("load")
        self.product_cards.nth(n).get_by_role("link", name="View Product").click()
        return ProductDetailPage(self.page)

    def search_products(self, search_term):
        self.search_textbox.fill(search_term)
        self.search_button.click()
