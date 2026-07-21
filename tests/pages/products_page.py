from playwright.sync_api import Page
from tests.pages.components.product_list import ProductList


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.products = ProductList(page)
        self.page.wait_for_load_state("load")
