from tests.pages.base_page import BasePage
from tests.pages.components.product_list import ProductList


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.products = ProductList(page)

    def open(self):
        self.page.goto("/", wait_until="domcontentloaded")
