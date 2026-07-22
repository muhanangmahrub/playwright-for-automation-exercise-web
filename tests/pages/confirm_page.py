from playwright.sync_api import Page


class ConfirmPage:
    def __init__(self, page: Page):
        self.page = page
        self.order_placed_heading = page.get_by_text("Order Placed!")
        self.order_confirmation_message = page.get_by_text(
            "Congratulations! Your order"
        )
        self.download_invoice_link = page.get_by_role("link", name="Download Invoice")
        self.continue_link = page.get_by_role("link", name="Continue")

    def click_continue(self):
        self.continue_link.click()
