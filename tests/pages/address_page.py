from playwright.sync_api import Page
from tests.pages.payment_page import PaymentPage


class AddressPage:
    def __init__(self, page: Page):
        self.page = page

    def place_order(self):
        self.page.locator('textarea[name="message"]').fill("Test")
        self.page.get_by_role("link", name="Place Order").click()
        return PaymentPage(self.page)
