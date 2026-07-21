from playwright.sync_api import Page
from tests.pages.cart_page import CartPage
from tests.pages.product_detail_page import ProductDetailPage


class ProductList:
    def __init__(self, page: Page):
        self.page = page

    def continue_shopping(self):
        self.page.get_by_role("button", name="Continue Shopping").click()

    def add_nth_product_to_cart(self, n: int):
        products = self.page.locator(".features_items .product-image-wrapper")
        products.nth(n).locator(".productinfo").get_by_text("Add to cart").click()

    def view_cart(self):
        self.page.get_by_role("link", name="View Cart").click()
        return CartPage(self.page)

    def view_product_details_of_nth_product(self, n: int):
        self.page.wait_for_load_state("load")
        products = self.page.locator(".features_items .product-image-wrapper")
        products.nth(n).get_by_role("link", name="View Product").click()
        return ProductDetailPage(self.page)

    def search_products(self, search_term):
        self.page.get_by_role("textbox", name="Search Product").fill(search_term)
        self.page.locator("#submit_search").click()
