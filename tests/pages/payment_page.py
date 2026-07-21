from playwright.sync_api import Page
from tests.pages.confirm_page import ConfirmPage


class PaymentPage:
    def __init__(self, page: Page):
        self.page = page

    def fill_payment_details(
        self, name: str, card_number: str, cvc: str, month: str, year: str
    ):
        self.page.locator('input[name="name_on_card"]').fill(name)
        self.page.locator('input[name="card_number"]').fill(card_number)
        self.page.get_by_role("textbox", name="ex.").fill(cvc)
        self.page.get_by_role("textbox", name="MM").fill(month)
        self.page.get_by_role("textbox", name="YYYY").fill(year)
        self.page.get_by_role("button", name="Pay and Confirm Order").click()
        return ConfirmPage(self.page)
