from playwright.sync_api import Page
from tests.pages.payment_page import PaymentPage


class AddressPage:
    def __init__(self, page: Page):
        self.page = page
        self.address_details_heading = page.get_by_role(
            "heading", name="Address Details"
        )
        self.review_order_heading = page.get_by_role(
            "heading", name="Review Your Order"
        )
        self.message_textarea = page.locator('textarea[name="message"]')
        self.place_order_link = page.get_by_role("link", name="Place Order")

    def place_order(self):
        self.message_textarea.fill("Test")
        self.place_order_link.click()
        return PaymentPage(self.page)
